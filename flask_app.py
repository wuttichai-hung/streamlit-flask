from flask import Flask, request, jsonify
from tensorflow.keras.applications.inception_v3 import InceptionV3, decode_predictions
import numpy as np
import cv2

app = Flask(__name__)

# Load the model
# model = tf.keras.models.load_model('my_model.h5')
model = InceptionV3()


@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded file
    file = request.files['file']

    # Read the image and preprocess it
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), -1)
    img = cv2.resize(img, (299, 299))
    img = img.astype('float32') / 255.0

    # Make a prediction using the model
    prediction = model.predict(img.reshape(1, 299, 299, 3))
    decoded_pred = decode_predictions(prediction)[0]
    # Return the prediction as a JSON object
    return jsonify({'prediction': [(t[1], t[2].item()) for t in decoded_pred]})


if __name__ == '__main__':
    app.run(debug=True)
