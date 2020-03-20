import pandas as pd

def createDatabase():
  df = pd.DataFrame({"IG Handle": ["@"], 'Date Started Following': ['-'], 'First Name': ['-'],
                       'Last Name': ['-'], 'Home State': ['-'], 'Home City': ['-'], 'Aprx Household Income': ['-'],
                       'Date of Last Story View': ['-'], 'Date of Last Story Engagement': ['-'], '# of Story Engagements': ['-'],
                       '# of Story Swipe Ups': ['-'], 'Date of Last Post Engagement': ['-'], '# of Post Engagements': ['-'],
                       '# Post Likes': ['-'], '# of Post Comments': ['-'], 'Response to Story Question Stickers': ['See Following columns']
                       })
  datatoexcel = pd.ExcelWriter("../database/InstagramData.xlsx", engine="xlsxwriter")
  df.to_excel(datatoexcel, sheet_name="sheet1")
  datatoexcel.save()

def populateDatabase(name, stickerQuestion, response):
  df = pd.read_excel('../database/InstagramData.xlsx', index_col=[0])

  foundIGHandle = df[df['IG Handle'].str.contains(name)]
  IGHandlecount = foundIGHandle.count()[-1]

  # if (IGHandlecount == 0):
  df2 = pd.DataFrame({"IG Handle": [f"@{name}"], 'Date Started Following': ['-'], 'First Name': ['-'],
                    'Last Name': ['-'], 'Home State': ['-'], 'Home City': ['-'], 'Aprx Household Income': ['-'],
                    'Date of Last Story View': ['-'], 'Date of Last Story Engagement': ['-'], '# of Story Engagements': ['-'],
                    '# of Story Swipe Ups': ['-'], 'Date of Last Post Engagement': ['-'], '# of Post Engagements': ['-'],
                    '# Post Likes': ['-'], '# of Post Comments': ['-'], 'Response to Story Question Stickers': ['->']})
  df2[stickerQuestion] = response
  df = df.append(df2, ignore_index=True)

  datatoexcel = pd.ExcelWriter("../database/InstagramData.xlsx", engine="xlsxwriter")
  df.to_excel(datatoexcel, sheet_name="sheet1")
  datatoexcel.save()
