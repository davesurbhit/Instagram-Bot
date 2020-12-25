# imports
from instapy import InstaPy
from instapy import smart_run
import json
from time import sleep
from secrets import pw

# login credentials
insta_username = #Enter username
insta_password = pw #Enter password of the account in secrets.py file



# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  your_followers = session.grab_followers(username='''Enter username of the acc''', amount="full", live_match=True, store_locally=True)

