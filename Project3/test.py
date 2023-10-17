import joblib
import json
import numpy as np
import base64
import cv2
from wavelet import w2d

def classify_image(file_path=None):

    imgs = get_cropped_image_if_2_eyes(file_path)

    result = []
    img=imgs[0]
    scalled_raw_img = cv2.resize(img, (32, 32))
    img_har = w2d(img, 'db1', 5)
    scalled_img_har = cv2.resize(img_har, (32, 32))
    combined_img = np.vstack((scalled_raw_img.reshape(32 * 32 * 3, 1), scalled_img_har.reshape(32 * 32, 1)))

    len_image_array = 32 * 32 * 3 + 32 * 32

    final = combined_img.reshape(1, len_image_array).astype(float)

    return final


def get_cropped_image_if_2_eyes(image_path):
    face_cascade = cv2.CascadeClassifier("C:\\Users\\mirzadsr\\AppData\\Roaming\\Python\\Python311\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier('C:\\Users\\mirzadsr\\AppData\\Roaming\\Python\\Python311\\site-packages\\cv2\\data\\haarcascade_eye.xml')


    img = cv2.imread(image_path)


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)

    cropped_faces = []
    for (x,y,w,h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
 #           if len(eyes) >= 1:
            cropped_faces.append(roi_color)
    print(cropped_faces)
    return cropped_faces


with open('./artifacts/model_pickle.pkl', 'rb') as f:
    __model = joblib.load(f)

image="C:\\Users\\mirzadsr\\Downloads\\images (7).jpg"

print(classify_image(image).shape)
final=__model.predict(classify_image(image))
prob=np.round(__model.predict_proba(classify_image(image))*100,2)[0]
formatted_strings=[]
classes=["Katy Perry","Rihanna","Lady Gaga","Beyonce"]
class_probabilities = dict(zip(classes, prob))
formatted_string = "\n".join([f"{cls}: {prob:.2f}" for cls, prob in class_probabilities.items()])
formatted_strings.append(formatted_string)
# Join the formatted strings for each prediction
resulting_string = "\n\n".join(formatted_strings)

print(resulting_string)

print(class_probabilities)

