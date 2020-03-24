import json
import pyautogui
from random import randint
import pandas as pd
import re
import tkinter as tk
import math
from datetime import datetime
from dateutil.parser import parse

with open('/Users/Tanner/Downloads/data.json') as f:
  data = json.load(f)

rawFollowers = data['followers']
prettyFollowers = json.dumps(rawFollowers, indent=4)

rawBlockedUsers = data['blocked_users']
prettyFollowers = json.dumps(rawBlockedUsers, indent=4)

rawRestricedUsers = data['restricted_users']
prettyFollowers = json.dumps(rawRestricedUsers, indent=4)

rawFollowRequestsSent = data['follow_requests_sent']
prettyFollowers = json.dumps(rawFollowRequestsSent, indent=4)

rawFolloring = data['following']
prettyFollowers = json.dumps(rawFolloring, indent=4)

rawFollowingHashtags = data['following_hashtags']
prettyFollowers = json.dumps(rawFollowingHashtags, indent=4)

rawWhitelistedForSponsorTaggingBy = data['whitelisted_for_sponsor_tagging_by']
prettyFollowers = json.dumps(rawWhitelistedForSponsorTaggingBy, indent=4)

rawDismissedSuggestedUSers = data['dismissed_suggested_users']
prettyFollowers = json.dumps(rawDismissedSuggestedUSers, indent=4)

df = pd.DataFrame({"IG Handle": ["---"], 'Date Started Following': ['-'], 'First Name': ['-'],
                   'Last Name': ['-'], 'Home State': ['-'], 'Home City': ['-'], 'Aprx Household Income': ['-'],
                    'Date of Last Story View': ['-'], 'Date of Last Story Engagement': ['-'], '# of Story Engagements': ['-'],
                    '# of Story Swipe Ups': ['-'], 'Date of Last Post Engagement': ['-'], '# of Post Engagements': ['-'],
                    '# Post Likes': ['-'], '# of Post Comments': ['-'], 'Response to Story Question Stickers': ['->']})

for index, follower in enumerate(rawFollowers):
  df1 = pd.DataFrame({
    "IG Handle": [follower[0]],
    'Date Started Following': ['-']
    })
  df = df.append(df1, ignore_index=True)
  print(index)

datatoexcel = pd.ExcelWriter(
    "./Users/Tanner/Downloads/InstagramFollowerData.xlsx", engine="xlsxwriter")
df.to_excel(datatoexcel, sheet_name="sheet1")
datatoexcel.save()

# parse(follower[1]).date()
