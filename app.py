from flask import Flask, jsonify, request, render_template
import os
from flask_cors import CORS
from src.classifier.pipeline.predict import PredictionPipeline
from classifier.utils.common import decodeImage as decode_image
from pathlib import Path

os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self, app):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(model_path=os.path.join("artifacts", "training", "trained_model.h5"))

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/train", methods=["GET", "POST"])
def train():
    os.system("python main.py")
    return "Training successful!"

@app.route("/predict", methods=["POST"])
def predictRoute():
    image = request.json["image"]
    decode_image(imgstring=image, fileName=clApp.filename)
    result = clApp.classifier.predict(img_path=clApp.filename)
    return jsonify(result)

if __name__ == "__main__":
    clApp = ClientApp(app)
    app.run(host="0.0.0.0", port=8080)