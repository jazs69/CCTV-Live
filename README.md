# 📹 CCTV Live Stream with Flask

A lightweight web app to stream **live video from your webcam or IP camera** directly in your browser — built using **Python**, **OpenCV**, and **Flask**.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🚀 Features

- 🔴 **Live streaming** from webcam or IP camera
- 💻 Simple browser-based interface
- 🧩 Modular code — easy to extend or modify
- 🛠️ Lightweight and minimal dependencies

---

## 🧰 Requirements

- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://pypi.org/project/Flask/)
- [OpenCV (`cv2`)](https://pypi.org/project/opencv-python/)

  Install all dependencies with:

  pip install flask opencv-python

## 📁 Project Structure

cctv-live-stream/
├── app.py               # Main Flask app
├── camera.py            # Handles video capture (OpenCV)
├── templates/
│   └── index.html       # Frontend template
└── README.md            # You're here!

## ⚙️ Configuration

  By default, the app uses your default webcam (cv2.VideoCapture(0)).

  To use an IP camera, edit camera.py:

# Change this:
  cv2.VideoCapture(0)

# To something like:
  cv2.VideoCapture("http://<IP_ADDRESS>:<PORT>/video")

## 💡 How to Run

1. Clone or download the project:

  git clone https://github.com/your-username/cctv-live-stream.git
  cd cctv-live-stream

2. Run the app:

  python app.py

3. Open your browser and go to:

  http://localhost:5000/
  
You should now see your live video feed! 🎉

## 🖼️ Screenshot

![alt text](image.png)

## 📜 License

This project is licensed under the MIT License
Use it freely for learning, demos, or extending your own projects!

## 🙋‍♂️ Contributing

Found an issue or have a feature idea?
Feel free to open an issue or a pull request.

### 💬 "Streaming made simple with Flask and OpenCV!"

---

Let me know if you'd like a logo, deploy button (for Heroku or Replit), or setup guide for IP cameras too!
