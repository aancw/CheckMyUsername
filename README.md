# CheckMyUsername
Python Library for Social Media and Other Service Username Availability Checker

## Install
```
git clone https://github.com/aancw/CheckMyUsername.git
pip2 install -r requirements.txt
python check_my_username.py --help
```

## Library Usage
If you want using this for your library, you can simply add like this:

```
from CheckMyUsername.check_my_username import CheckMyUsername

user_check = CheckMyUsername()
print(user_check.check_username_availability("blablabla"))
```

## What this tool can do?

Checking username for various service:

- Facebook
- GitHub
- Medium
- BitBucket
- Instagram
- Twitter
- Medium
- Steam( on progress )
- etc

## Why I Made this?

I need username checker library for my tool, you can check at https://github.com/aancw/Belati.git

## Dependencies
urllib2
argparse

## Author
Aan Wahyu a.k.a Petruknisme(https://petruknisme.com)

## License
CheckMyUsername is licensed under GPL V2. You can use, modify, or redistribute this tool under the terms of GNU General Public License (GPLv2).
