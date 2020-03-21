import io
import os
import json
import glob
import pandas as pd

from database import createDatabase, populateDatabase
from splitImage import createSubImages
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'../APIKey.json'

client = vision.ImageAnnotatorClient()

for filename in os.listdir('/Users/Tanner/code/products/Instagram/uncroppedImages'):
  image_file = os.path.join('/Users/Tanner/code/products/Instagram/uncroppedImages', filename)
  createSubImages(f"{image_file}")

def populate():
  for filepath in glob.iglob('/Users/Tanner/code/products/Instagram/croppedImages/*'):
    file_name = os.path.abspath(f"{filepath}")
    with io.open(file_name, 'rb') as image_file:
      content = image_file.read()
      image = types.Image(content=content)
      response = client.document_text_detection(image=image)
      text = response.text_annotations
      username = text[0].description.split('\n')[0]
      textBody = text[0].description.split('\n')[1:]
      newText = str("".join(textBody))
      # print(newText)

      if (os.path.exists('../database/InstagramData.xlsx') == False):
        createDatabase()
      
      populateDatabase(username, 'Add Question', newText)

populate()
