from PIL import Image
from datetime import datetime

def createSubImages(picture):
  
  im = Image.open(picture)

  boxes = {
    'one': {
      'left': 5,
      'top': 120,
      'right': 280,
      'bottom': 320
    },
    'two': {
        'left': 280,
        'top': 120,
        'right': 540,
        'bottom': 320
    },
    'three': {
        'left': 5,
        'top': 400,
        'right': 280,
        'bottom': 600
    },
    'four': {
        'left': 280,
        'top': 400,
        'right': 540,
        'bottom': 600
    },
    'five': {
        'left': 5,
        'top': 650,
        'right': 280,
        'bottom': 830
    },
    'six': {
        'left': 280,
        'top': 650,
        'right': 540,
        'bottom': 830
    },
    'seven': {
        'left': 5,
        'top': 920,
        'right': 280,
        'bottom': 1120
    },
    'eight': {
        'left': 280,
        'top': 920,
        'right': 540,
        'bottom': 1120
    }
  }

  for x in range(len(boxes)):
    key = (list(boxes.keys())[x])
    croppedImg = im.crop((boxes[f"{key}"]['left'], boxes[f"{key}"]['top'],
             boxes[f"{key}"]['right'], boxes[f"{key}"]['bottom']))
    croppedImg.save(f"/Users/Tanner/code/products/Instagram/croppedImages/{key}.jpg")

createSubImages("/Users/Tanner/code/products/Instagram/uncroppedImages/insta.jpg")
