from flask import Flask, render_template, request
import joblib
import numpy as np
import util


app = Flask(__name__, static_folder="static")


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

    # Sort the class_probabilities dictionary by probabilities in descending order
    sorted_class_probabilities = dict(sorted(class_probabilities.items(), key=lambda x: x[1], reverse=True))

    # Create a list of strings for predictions in descending order with "%" sign
    predictions_list = [f"{cls}: {prob:.2f}" for cls, prob in sorted_class_probabilities.items()]

    return render_template('next_page.html', predictions=predictions_list)


if __name__ == '__main__':
    app.run(port=5000, debug=True)