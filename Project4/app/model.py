import tensorflow as tf
import numpy as np

# Load the pre-trained model from the .h5 file
model = tf.keras.models.load_model('tomatoes.h5')

CLASS_NAMES=['Tomato_Bacterial_spot',
 'Tomato_Early_blight',
 'Tomato_Late_blight',
 'Tomato_Leaf_Mold',
 'Tomato_Septoria_leaf_spot',
 'Tomato_Spider_mites_Two_spotted_spider_mite',
 'Tomato__Target_Spot',
 'Tomato_YellowLeaf__Curl_Virus',
 'Tomato_mosaic_virus',
 'Tomato_healthy']
def recognize_image(image):
    img_batch = np.expand_dims(image, 0)

    predictions = model.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }
