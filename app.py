from flask import Flask, jsonify, request, render_template
import os
import uuid
from flask_cors import CORS
from src.classifier.pipeline.predict import PredictionPipeline
from src.classifier.utils.common import decodeImage as decode_image

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        # Dictionary of potential paths to check
        self.model = None
        paths_to_check = [
            os.path.join("artifacts", "training", "trained_model.h5"),
            "trained_model.h5",
            os.path.join(os.getcwd(), "trained_model.h5")
        ]
        
        model_path = None
        for path in paths_to_check:
            if os.path.exists(path):
                model_path = path
                print(f"Model found at: {model_path}")
                break
        
        if model_path:
            self.classifier = PredictionPipeline(model_path=model_path)
        else:
            print(f"CRITICAL: Model file not found. Checked: {paths_to_check}")
            # We don't raise here to allow the app to start, but predictions will fail
            self.classifier = None

clApp = None
try:
    clApp = ClientApp()
except Exception as e:
    print(f"CRITICAL ERROR LOADING MODEL: {e}")
    # clApp stays None or partially initialized


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/train", methods=["GET", "POST"])
def train():
    os.system("python main.py")
    return "Training successful! (Note: Changes are temporary on Cloud Run)"

@app.route("/predict", methods=["POST"])
def predictRoute():
    try:
        if os.name == 'posix': # Linux/Mac/Cloud Run
            base_path = "/tmp"
        else: # Windows
            base_path = "uploads"
            if not os.path.exists(base_path):
                os.makedirs(base_path)

        filename = str(uuid.uuid4()) + ".jpg"
        filepath = os.path.join(base_path, filename)

        if "file" in request.files:
            file = request.files["file"]
            if file.filename == "":
                return jsonify({"error": "No file selected"}), 400
            file.save(filepath)

        elif request.is_json:
            data = request.get_json()
            if "image" not in data:
                return jsonify({"error": "Missing image data"}), 400
            decode_image(imgstring=data["image"], fileName=filepath)

        else:
            return jsonify({"error": "Unsupported request"}), 400

        if clApp is None or clApp.classifier is None:
            return jsonify({"error": "Model not loaded. Please contact administrator."}), 500

        result = clApp.classifier.predict(img_path=filepath)
        
        if os.path.exists(filepath):
            os.remove(filepath)

        return jsonify(result)

    except Exception as e:
        print(f"ERROR DURING PREDICTION: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)