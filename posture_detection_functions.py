import tensorflow as tf
import cv2
import numpy as np
import tensorflow_hub as hub
import tempfile

model = hub.load("https://tfhub.dev/google/movenet/singlepose/thunder/4")
movenet = model.signatures['serving_default']
model = tf.keras.models.load_model('modelV3.h5')

async def save_temp_file(file):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(await file.read())
        temp_file_name = temp.name
    return temp_file_name

def extract_video_features(temp_file_name):
    cap = cv2.VideoCapture(temp_file_name)
    video_features = []
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            image = tf.image.resize(frame, [256, 256])
            image = tf.cast(image, dtype=tf.int32)
            image = tf.expand_dims(image, axis=0)
            outputs = movenet(image)
            video_features.append(outputs['output_0'].numpy())
        else:
            break
    cap.release()
    return video_features

def preprocess_features(video_features):
    #features = np.mean(video_features, axis=0)
    #features = np.expand_dims(features, axis=0)
    features_array = np.array(video_features)
    print(features_array.shape)
    #features = np.reshape(features, (1, 17, 3, 1))
    return features_array

def predict_class(features):
    predictions = model.predict(features)
    return predictions