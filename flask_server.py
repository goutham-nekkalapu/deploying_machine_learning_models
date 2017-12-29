
import PIL
import numpy as np
import argparse,urllib
from PIL import Image, ImageOps
import requests
from keras import backend as K
K.set_image_dim_ordering('tf')

import os
from io import StringIO
from io import BytesIO
import json

# importing the functions of prediction model 
from model import *

from flask import Flask, request, redirect, url_for,make_response,jsonify
app=Flask(__name__)

# if we are using the InceptionV3 or Xception networks, then we
# need to set the input shape to (299x299) [rather than (224x224)]
# and use a different image processing function
def load_img(path, grayscale=False, target_size=None):
    response = requests.get(path)
    img = Image.open(StringIO(response.content)).resize((224,224))
    print (img)
    if grayscale:
        if img.mode != 'L':
            img = img.convert('L')
    else:
        if img.mode != 'RGB':
            img = img.convert('RGB')
    if target_size:
        wh_tuple = (target_size[1], target_size[0])
        if img.size != wh_tuple:
            img = img.resize(wh_tuple)
    return img

def read_image_from_url(url):
    response = requests.get(url, stream=True)
    img = Image.open(BytesIO(response.content))
    img=img.resize((224,224), PIL.Image.ANTIALIAS).convert('RGB')
    print (img)
    return img

def read_image_from_ioreader(image_request):
    img = Image.open(BytesIO(image_request.read())).convert('RGB')
    return img

# to predict the top-5 food items 
@app.route('/api/v1/classify_image_top_5', methods=['POST'])
def classify_image_top_5():
    print("-------------------------------------------")
    if 'image' in request.files:
        print("Image request")
        image_request = request.files['image']
        img = read_image_from_url(image_request)
    elif 'url' in request.json:
        print("JSON request: ", request.json)
        image_url = request.json['url']
        print (image_url)
        img = read_image_from_url(image_url)
    else:
        abort(BAD_REQUEST)
    resp = predict_return_top_5(img)
    return make_response(jsonify(resp), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

