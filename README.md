# 🔬 Chemical-Pipelines-Corrosion-Detection-Deep-Learning
A deep learning-based corrosion detection system using MobileNetV2 and Flask for real-time image classification. The project detects corrosion in pipeline images and provides an interactive web interface for prediction.

## 📌 Overview

This project presents an automated corrosion detection system for pipeline images using deep learning. A MobileNetV2-based Convolutional Neural Network (CNN) is used to classify images as **Corroded** or **Normal**. The trained model is deployed using Flask to provide a user-friendly web interface for real-time prediction.

---

## 🚀 Features

* Deep Learning-based corrosion detection
* Transfer learning using MobileNetV2
* Image upload and real-time prediction
* Confusion matrix evaluation
* Grad-CAM heatmap visualization
* Lightweight and efficient model

---

## 🧠 Model Architecture

The model uses MobileNetV2 as a feature extractor followed by:

* Global Average Pooling
* Dense Layer (ReLU)
* Output Layer (Sigmoid)

---

## 📊 Results

* Accuracy: ~98–100%
* Effective corrosion detection
* Visual explanation using Grad-CAM

---

## 🖥️ Web Application

* Built using Flask
* Upload image → Get prediction instantly
* Displays uploaded image + result

---

## 📁 Project Structure
```
Chemical-Pipelines-Corrosion-Detection-Deep-Learning/
├── app.py                      # Flask backend
├── corrosion_model.h5          # Trained DL model
├── requirements.txt            # Dependencies
├── README.md                   # Project documentation
├── templates/
│   └── index.html              # Frontend UI
├── Pipeline Corrosion Detection Dataset/                   
│   ├── train/
│       ├── corroded/
│       └── normal/
│   └── test/
│       ├── corroded/
│       └── normal/
└── notebook/
    └── dl_project.ipynb        
```


---

## ⚙️ Installation

# Install dependencies
```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

## 📌 Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* Flask
* NumPy, Matplotlib

---

## 🔍 Future Improvements

* Multi-class corrosion detection
* Real-time monitoring using cameras
* IoT integration
* Model optimization for edge devices

---

## 👨‍💻 Author
**Dev Patel**

---

## 👨‍💻 Contribution
This project was fully developed independently, including dataset preparation, model implementation, and interface development.
