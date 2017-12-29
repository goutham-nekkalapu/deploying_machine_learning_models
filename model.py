
from keras.applications import VGG19
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions

from keras.applications import imagenet_utils
from keras.preprocessing.image import img_to_array

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

import numpy as np 
inputShape = (224, 224)
preprocess = imagenet_utils.preprocess_input

# helper fun, to convert predictions to lists and 
# update them to a dictionary 
def convert_to_lists(P):
    output = {} 
    for (i, (imagenetID, label, prob)) in enumerate(P[0]):
            label = label.lower()
            label = label.replace("_"," ")
            temp = {}
            temp[i+1] = [label, str(prob)]
            output.update(temp)
    return output

Network = ResNet50
model = Network(weights="imagenet")
graph = tf.get_default_graph()

def predict_return_top_5(image):
    image1 = image
    image1 = img_to_array(image1)
    image1 = np.expand_dims(image1, axis=0)

    # pre-process the image using the appropriate function based on the
    # model that has been loaded (i.e., mean subtraction, scaling, etc.)
    image1 = preprocess(image1)

    # classify the image
    global graph
    with graph.as_default():
        preds = model.predict(image1)

    print('Predicted:', decode_predictions(preds, top=3)[0])
    P = imagenet_utils.decode_predictions(preds)

    # priting for debugging at server side 
    for (i, (imagenetID, label, prob)) in enumerate(P[0]):
                print("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))

    # converting top-5 prediction to dictionaries
    P = convert_to_lists(P)
    return P
                                                                                                                                       

