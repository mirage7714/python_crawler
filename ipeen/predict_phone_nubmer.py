
# coding: utf-8

import numpy as np
import pandas as pd
import imutils
import pickle
from imutils import paths
from keras.models import load_model
import cv2
from skimage import data, io
import glob
import warnings
import os
import tensorflow as tf
import os.path
warnings.filterwarnings("ignore")

# Enable gpu to grow memory usage. 
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

model_filename = 'model/phone_number_model.hdf5'
model_labels_filename = 'model/model_labels.dat'

with open(model_labels_filename, 'rb') as f:
    lb = pickle.load(f)

model = load_model(model_filename)
number_image_file = 'web_content/temp.png'

def resize_to_fit(image, width, height):

    padW = int((width - image.shape[1]) / 2.0)
    padH = int((height - image.shape[0]) / 2.0)

    image = cv2.copyMakeBorder(image, padH, padH, padW, padW,
        cv2.BORDER_REPLICATE)
    image = cv2.resize(image, (width, height))

    return image

def Check(data):
    if (data.mean() >= 233.75 ):
        return 0
    else:
        return 1

def AddPixels(data, width):
    pixels = []
    for num in range(0, width):
        d = data[:][num]
        is_valid = Check(d)
        if (is_valid == 1):
            pixels.append(num)
    return pixels

def GetChars(pixels):
    chars = []
    number = []
    for num in pixels:
        index = pixels.index(num)
        if(index != len(pixels)-1):
            if (pixels[index + 1] - num == 1 ):
                number.append(num)
            else:
                number.append(num)
                if(len(number) > 10):
                    char1 = []
                    char2 = []
                    for n in range(0, len(number)):
                        if (n< 8):
                            char1.append(number[n])
                        else:
                            char2.append(number[n])
                    chars.append(tuple(char1))
                    chars.append(tuple(char2))
                else:
                    chars.append(tuple(number))
                number.clear()
        else:
            chars.append(tuple(number))
    return chars

def CheckNumber():
    
    temp = 'temp/temp.png'
    filename = os.path.basename(number_image_file)
    photo_correct_text = os.path.splitext(filename)[0]
    phone_mod = ''
    for text in photo_correct_text:
        if (text != ' '):
            phone_mod += text
    image = data.imread(number_image_file)
    image_pd = pd.DataFrame(image)
    width = image_pd.shape[1]
    pixels = AddPixels(image_pd, width)
    empty = image_pd[width - 1]
    predictions = []
    chars = GetChars(pixels)
    for char in chars:
        ch = list(char)
        char_pd = image_pd[ch]
        for c in ch:
            char_pd[c] = char_pd[c].apply(lambda x : 0 if x < 255 else 255)
        char_pd[len(ch)] = empty
        io.imsave(temp, char_pd)
        num = cv2.imread(temp)
        num = cv2.cvtColor(num, cv2.COLOR_BGR2GRAY)
        num = resize_to_fit(num, 12, 12)
        num = np.expand_dims(num, axis = 2)
        num = np.expand_dims(num, axis = 0)
        pred = model.predict(num)
        letter = lb.inverse_transform(pred)[0]
        predictions.append(letter)
    pred_phone = ''
    for prediction in predictions:
        pred_phone = pred_phone+''+prediction

    return pred_phone



