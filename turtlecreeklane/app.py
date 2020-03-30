import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from python.connections import createDatabaseAndPopulateWithFollowersDateAndTime, createSubImages, populate

app = Flask(__name__)
CORS(app)

@app.route("/submit/", methods=["POST"])
def submit():
  if request.method == "POST":
    if 'file' in request.files:
      json_file = request.files['file']
      saved_name = os.path.join(
          "/Users/Tanner/code/products/Instagram/turtlecreeklane/", json_file.filename)
      json_file.save(saved_name)
      createDatabaseAndPopulateWithFollowersDateAndTime(saved_name)
    else:
      print("file not present")
  print("sucess")
  return jsonify(status='200')

@app.route('/stickers/', methods=["POST"])
def stickers():
  if request.method == "POST":
    if 'file' in request.files:
      json_file = request.files['file'][0]
      saved_name = os.path.join("/Users/Tanner/code/products/Instagram/turtlecreeklane/", json_file.filename)
      
      for file in request.files:
        createSubImages(file)
      
      populate()

    else:
      print('file not present')
  print('success')
  return jsonify(status='200')

