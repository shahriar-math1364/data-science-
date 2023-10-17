from flask import Flask, render_template, request
import joblib
import numpy as np
import util
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
#from keras.applications.vgg16 import VGG16
from keras.applications.resnet50 import ResNet50

app = Flask(__name__)
model = ResNet50()

@app.route('/', methods=['GET'])
def hello_word():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile= request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)
    with open('./artifacts/model_pickle.pkl', 'rb') as f:
        __model = joblib.load(f)
    prob=np.round(__model.predict_proba(util.classify_image(image_path))*100,2)[0]
    pred=__model.predict(util.classify_image(image_path))
 #  dic={0:'Katy Perry', 1:'Rihanna', 2:'Lady Gaga', 3:'Beyonce'}
    formatted_strings = []
    classes = ["Katy Perry", "Rihanna", "Lady Gaga", "Beyonce"]
    class_probabilities = dict(zip(classes, prob))
    formatted_string = "\n".join([f"{cls}: {prob:.2f}" for cls, prob in class_probabilities.items()])
    formatted_strings.append(formatted_string)
    resulting_string = "\n\n".join(formatted_strings)

    return render_template('index.html', prediction=resulting_string)


if __name__ == '__main__':
    app.run(port=1000, debug=True)