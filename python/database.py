# import pymongo
# from pymongo import MongoClient
import pandas as pd

# cluster = MongoClient("mongodb+srv://houta483:Pitbull92929@instagram-42vnx.mongodb.net/test?retryWrites=true&w=majority")
# db = cluster['Instagram']
# collection = db['InstagramHoughton']
# post = {
#   'test': 'First test',
#   'secondTest': 'second test'
# }
# collection.insert_one(post)

def inputData(name, comment):
  data = pd.DataFrame({"instagramUsers": [name], 'Comments': [comment]})
  datatoexcel = pd.ExcelWriter("InstagramData.xlsx", engine="xlsxwriter")
  data.to_excel(datatoexcel, sheet_name="sheet1")
  datatoexcel.save()
