from flask import Flask, jsonify, request

from tensorflow import keras
from tensorflow.keras.layers import Conv2D, BatchNormalization, \
                                    AveragePooling2D, Dense, Activation, \
                                    Flatten, Dropout
from tensorflow.keras import Sequential
import json, io 
from PIL import Image
import numpy as np

app = Flask(__name__)
model = keras.models.load_model('./model/mnist_cnn.h5')

@app.route("/predict", methods=['POST'])
def predict():
    file = request.files['image_file']
    file_bin = file.read()
    image = Image.open(io.BytesIO(file_bin))
    return {'filename':file.filename, 'prediction':run_model(model, image)}

def run_model(model, image):
    np_img = np.asarray(image)
    np_img = np.expand_dims(np_img, 0)
    np_img = np.expand_dims(np_img, 0)
    pred = np.argmax(model.predict(np_img), axis=1)
    return str(pred[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0')