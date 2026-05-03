from flask import Flask, render_template, request
import cv2
import numpy as np
import base64
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load model ONLY
model = load_model("corrosion_model.h5")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_data = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            file_bytes = np.frombuffer(file.read(), np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            _, buffer = cv2.imencode('.jpg', img)
            image_data = base64.b64encode(buffer).decode('utf-8')

            img = cv2.resize(img, (224,224))
            img = img / 255.0
            img = np.expand_dims(img, axis=0)

            pred = model.predict(img)[0][0]

            if pred > 0.5:
                result = "Normal"
            else:
                result = "Corroded"

    return render_template("index.html", result=result, image_data=image_data)


if __name__ == "__main__":
    import threading
    import webbrowser

    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000")

    # Open browser after slight delay
    threading.Timer(1, open_browser).start()
    
    app.run(debug=True, use_reloader=False)