import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, model_path, target_size=(224, 224)):
        # 1. Verification: Ensure model actually exists before trying to load
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at: {model_path}")
            
        self.model = load_model(model_path)
        self.target_size = target_size

    def predict(self, img_path):
        # 2. Loading: 'img_path' will be a temporary path in /tmp (safe for Cloud Run)
        test_image = image.load_img(img_path, target_size=self.target_size)
        
        # 3. Conversion: Convert PIL image to NumPy array
        test_image = image.img_to_array(test_image)
        
        # 4. Batching: Expand dims to make it (1, 224, 224, 3)
        test_image = np.expand_dims(test_image, axis=0)

        # =========================================================================
        # CRITICAL CHECK: Normalization
        # Most models trained on standard data need inputs between 0 and 1.
        # If your training code used `Rescaling(1./255)`, UNCOMMENT the line below.
        # If you leave this commented out and your model expects 0-1, 
        # your predictions will be wrong (random).
        
        test_image = test_image / 255.0
        # =========================================================================

        # 5. Prediction
        probs = self.model.predict(test_image)
        result_index = np.argmax(probs, axis=1)[0]
        confidence = float(np.max(probs, axis=1)[0])

        # 6. Labels: Using a dictionary is cleaner and faster than if-else
        label_map = {
            0: 'You have Glioma Brain Tumor, Get urgent attention!',
            1: 'You are healthy',
            2: 'You have Meningioma Brain Tumor, Get urgent attention!',
            3: 'You have Pituitary Tumor, Get urgent attention!'
        }
        
        prediction = label_map.get(result_index, 'Unknown Label')

        return [{"prediction": prediction, "confidence": confidence}]