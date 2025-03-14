from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("fruit_classifier_model.h5")


class_names = ['apple', 'broccoli', 'grape', 'lemon', 'mango', 'orange', 'strawberry']


def preprocess_image(image):
    image = image.resize((128, 128))  # Resize to match model input
    image = np.array(image) / 255.0   # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return render_template("index.html", message="No file selected!")
        
        file = request.files["file"]
        if file.filename == "":
            return render_template("index.html", message="No file selected!")

        # Save the uploaded image
        filepath = os.path.join("static/uploads", file.filename)
        file.save(filepath)

        # Process the image and make a prediction
        image = Image.open(filepath)
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        predicted_class = class_names[np.argmax(prediction)]

        return render_template("index.html", prediction=predicted_class, image_path=filepath)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
