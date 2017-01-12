#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Python Library for Social Media and Other Service Username Availability Checker
#   Copyright (C) 2017  cacaddv@gmail.com (Petruknisme a.k.a Aan Wahyu)
#

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib2
import sys
import argparse
import re

class CheckMyUsername(object):

    def check_response_code(self, service_url, username):
        url = service_url + username
        request = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/49.0"})
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            if e.code == 404:
                return ("Available")
            else:
                return (e.code, e.reason)
        else:
            if response.getcode() == 200:
                return ("Already exists")

    def common_service_list(self, username):
        # Common Service List checker with URL Check
        serviceList = [['Github','https://github.com/'],['Facebook','http://facebook.com/'],['Instagram','https://instagram.com/'],['Twitter','https://twitter.com/'],['Bitbucket','https://bitbucket.org/'],['Medium','https://medium.com/@']]

        status_list = []

        for list in serviceList:
            if self.check_response_code(list[1], username) == "Already exists":
                status_list.append([username, list[0], "exist"])
            else:
                status_list.append([username, list[0], "available"])

        return status_list

    def check_steam_user(self, username):
        url = "https://steamcommunity.com/id/" + username
        request = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/49.0"})

        steam_status = []
        try:
            response = urllib2.urlopen(request)
            data = response.read()
            if re.findall('This profile is private.', data):
                steam_status = [username, 'Steam', 'private']
            elif re.findall('The specified profile could not be found.', data):
                steam_status = [username, 'Steam', 'notfound']
            else:
                steam_status = [username, 'Steam', 'exist']
        except urllib2.HTTPError as e:
            return (e.code, e.reason)

        return steam_status

    def check_username_availability(self, username):
        username_status = []
        username_status = self.common_service_list(username)
        username_status.append(self.check_steam_user(username))
        return username_status

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='=[ Check My Username v0.1-dev by Petruknisme]')
    parser.add_argument('-u', action='store', dest='username' , help='Username to be check')
    parser.add_argument('--version', action='version', version='=[ Check My Username v0.1-dev by Petruknisme]')
    results = parser.parse_args()

    username = results.username

    CheckMyUsernameApp = CheckMyUsername()
    username_status_result = CheckMyUsernameApp.check_username_availability(username)

    for result in username_status_result:
        print("Username " + result[0] + " for " + result[1] + " is " + result[2])
