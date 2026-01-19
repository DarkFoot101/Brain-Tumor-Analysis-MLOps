import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, model_path, target_size=(224, 224)):
        self.model = load_model(model_path)
        self.target_size = target_size

    def predict(self, img_path):
        model = load_model(os.path.join("artifacts", "training", "trained_model.h5"))
        imagename = img_path
        test_image = image.load_img(imagename, target_size= (224, 224))
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis= 1)
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
            return [{"image" : prediction}]
        else:
            prediction = 'Unhealthy'
            return [{"image" : prediction}]
