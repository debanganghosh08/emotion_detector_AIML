# 🎭 Emotion Detection & Voice Assistant

## 📝 Overview

This project is an AI-powered **Emotion Detection System** that uses **DeepFace** for facial expression recognition and **pyttsx3** for voice-based emotional support. It detects emotions in real-time through a webcam, tracks the user's face, and provides verbal suggestions based on detected emotions.

## 🔍 How It Works

1. The webcam captures live video.
2. The face is detected and tracked with a green bounding box.
3. When the user presses 'P', the system analyzes the face and predicts emotions.
4. Based on the detected emotion, a suggestion is displayed on the screen and spoken aloud.
5. The user can repeat the process by pressing 'P' or exit with 'Q'.

## ✋ Face Detection Logic

### ✋ Face Tracking with a Green Box

The **face detection** is performed using `DeepFace.analyze()` with the `enforce_detection=False` flag to avoid errors. The detected face is then enclosed within a **green bounding box**.

```python
result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)[0]
x, y, w, h = result['region']['x'], result['region']['y'], result['region']['w'], result['region']['h']
cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
```

### 🎭 Emotion Prediction on User Command

The **emotion detection** is activated when the user presses the 'P' key. The dominant emotion is extracted, and the system generates a suitable verbal suggestion.

```python
if key == ord('p'):
    predict_emotion = True

if predict_emotion:
    last_emotion = result['dominant_emotion']
    last_suggestion = emotion_suggestions.get(last_emotion, "Stay positive and take care!")
    emotion_display_time = time.time()
    tts_engine.say(last_suggestion)
    tts_engine.runAndWait()
    predict_emotion = False
```

## 💡 Detailed Code Breakdown

### 📌 Main Features

1. **Webcam Initialization & Optimization**

   - Adjusts resolution and FPS for better performance.
   - `cv2.VideoCapture(0)` opens the webcam.

2. **Face Detection & Tracking**

   - Uses `DeepFace.analyze()` for face & emotion recognition.
   - Draws a **green box** around the detected face.

3. **Emotion Prediction & Voice Suggestions**

   - On pressing 'P', the system analyzes the current facial expression.
   - Retrieves an emotion-specific **textual & voice response**.

4. **User Interaction Controls**

   - Press 'P' to analyze emotions.
   - Press 'Q' to quit the application.

## 📦 Requirements

Ensure you have the following dependencies installed before running the project:

```bash
pip install opencv-python numpy pyttsx3 deepface
```

## 🚀 How to Run the Project

1. Clone this repository:
   ```bash
   git https://github.com/debanganghosh08/emotion_detector_AIML.git
   cd emotion_detector_AIML
   ```
2. Install the required packages (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Python script:
   ```bash
   python emotion_ai.py
   ```
4. Press 'P' to predict emotions and get suggestions.
5. Press 'Q' to exit.

## 🏆 Features

✅ Real-time face detection 📷\
✅ Emotion recognition 😃😢😠😨\
✅ AI-generated suggestions 💡\
✅ Voice feedback using **pyttsx3** 🎤\
✅ User-controlled interactions 🔄

## 📌 Future Enhancements

🔹 Support for multiple faces 🤝\
🔹 Improved voice synthesis 🎙️\
🔹 Mobile & Web app integration 📱

---

### 🎯 Contribute & Support

Feel free to **fork** this repository, submit **pull requests**, or open **issues** for feature requests and bug fixes. If you like this project, don't forget to **⭐ star** the repository! 😃

