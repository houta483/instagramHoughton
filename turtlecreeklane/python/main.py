import io
import os, os.path
import json
import glob
import pandas as pd

from python.database import createDatabase, populateDatabase
from python.splitImage import createSubImages
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./python/APIKey.json'

client = vision.ImageAnnotatorClient()


def populate():
  count = 0
  for filepath in glob.iglob('/Users/Tanner/code/products/Instagram/croppedImages/*'):
    count = count + 1

    lengthOfDir = 0
    for name in os.listdir('../croppedImages'):
      lengthOfDir = lengthOfDir + 1

    print(str(round((count/lengthOfDir*100), 2)) + "%" + " Completed" )

    file_name = os.path.abspath(f"{filepath}")
    with io.open(file_name, 'rb') as image_file:
      content = image_file.read()
      image = types.Image(content=content)
      response = client.document_text_detection(image=image)
      text = response.text_annotations
      username = text[0].description.split('\n')[0]
      textBody = text[0].description.split('\n')[1:]
      newText = str("".join(textBody))
      newTextWithoutReply = newText.split('Reply')[0]

      if (os.path.exists('/Users/Tanner/code/products/Instagram/database/InstagramStickerResponseData.xlsx') == False):
        createDatabase()
        print('the database exists')
      populateDatabase(username, 'Add Question', newTextWithoutReply)

def prepareToRun():
  for filename in os.listdir('/Users/Tanner/code/products/Instagram/uncroppedImages'):
    image_file = os.path.join('/Users/Tanner/code/products/Instagram/uncroppedImages', filename)
    createSubImages(f"{image_file}")
  
  populate()
