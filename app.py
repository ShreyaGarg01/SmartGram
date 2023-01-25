from flask import Flask, render_template, request, Markup
import numpy as np
import requests
import pickle
import io
from PIL import ImageOps
from PIL import Image
# from werkzeug.datastructure import FileStorage
from werkzeug.utils import secure_filename
from keras.models import load_model
import h5py
import cv2
from io import BytesIO
import base64

# Trained Models loaded
crop_recommendation_model_path = 'models/RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))

# Trained Models loaded
plant_pathology_model_path = 'models/PlantPathology.hdf5'
plant_pathology_model = load_model(plant_pathology_model_path)

#  FLASK APP 
app = Flask(__name__)

# render home page
@ app.route('/')
def home():
    title = 'Home'
    return render_template('index.html', title=title)

@ app.route('/home')
def start():
    title = 'Home'
    return render_template('index.html', title=title)

# render crop recommendation form page
@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Crop Recommendation'
    return render_template('crop_recommendation.html', title=title)

# render crop recommendation form page
@ app.route('/plant-pathology')
def plant_pathology():
    title = 'Crop Recommendation'
    return render_template('plant_pathology.html', title=title)
# render crop recommendation form page
@ app.route('/weather-forecast')
def weather_forecast():
    title = 'Weather Forecast'
    # return render_template('weather_predication.html', title=title)
    return render_template('weather_forecast.html', title=title)


# RENDER PREDICTION PAGES

@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])

        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]
        return render_template('crop_prediction.html', prediction=final_prediction, title=title)

# main API code
@app.route('/plant-pathology', methods=['GET', 'POST'])
def pathology():
    title = 'Plant Pathology'
    if request.method == 'POST':
        file = request.files['file']

        filename = secure_filename(file.filename)
        print(filename)
        img = Image.open(file.stream)
        # with BytesIO() as buf:
        #     img.save(buf, 'jpeg')
        #     image_bytes = buf.getvalue()
        # encoded_string = base64.b64encode(image_bytes).decode()         
        image_data = img
        size = (128, 128)
        
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resize = (cv2.resize(img, dsize=(128, 128), interpolation=cv2.INTER_CUBIC))/255.
        
        data = img_resize[np.newaxis,...]
        
        my_prediction = plant_pathology_model.predict(data)
        final_prediction  = ""
        max_idx = np.argmax(my_prediction)
        if max_idx == 0:
            final_prediction = "is Healthy!"
        elif max_idx == 1:
            final_prediction = "has Multiple Diseases!"
        elif max_idx == 2:
            final_prediction = "has Rust!"
        else: 
            final_prediction = "has Scab!"
        print(my_prediction)
        return render_template('plant_pathology.html', prediction=final_prediction, title=title)

if __name__ == '__main__':
    app.run(debug = True)
