import cv2
import numpy as np
import pyttsx3
import time
from deepface import DeepFace

# Initialize text-to-speech
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 150)

# Define emotion-based suggestions
emotion_suggestions = {
    "angry": "You look angry! Take deep breaths and relax.",
    "happy": "You seem happy! Keep smiling and enjoy your day.",
    "sad": "You look sad. Try talking to someone or doing something fun.",
    "surprise": "You look surprised! Hope it's something good.",
    "neutral": "You seem neutral. Stay positive!",
    "fear": "You seem fearful. Stay strong, everything will be fine.",
    "disgust": "You look disgusted. Try focusing on something pleasant."
}

# Open webcam (Optimized)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Half screen width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)  # Half screen height
cap.set(cv2.CAP_PROP_FPS, 30)  # Limit FPS to reduce lag

predict_emotion = False  # Flag to control prediction
last_emotion = None
last_suggestion = ""
emotion_display_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert key press to lowercase for consistency
    key = cv2.waitKey(1) & 0xFF

    # If "p" is pressed, enable emotion detection
    if key == ord('p'):
        predict_emotion = True

    # Track face continuously
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)[0]
        x, y, w, h = result['region']['x'], result['region']['y'], result['region']['w'], result['region']['h']

        # Draw green box around face at all times
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if predict_emotion:
            last_emotion = result['dominant_emotion']
            last_suggestion = emotion_suggestions.get(last_emotion, "Stay positive and take care!")
            emotion_display_time = time.time()  # Set display timer

            # Speak the suggestion
            tts_engine.say(last_suggestion)
            tts_engine.runAndWait()

            predict_emotion = False  # Reset flag
            print("\nPress 'P' to predict again or 'Q' to quit.")

    except Exception as e:
        pass  # Ignore errors if no face is detected

    # Display last detected emotion for 5 seconds
    if last_emotion and time.time() - emotion_display_time < 5:
        cv2.putText(frame, f"{last_emotion.upper()}", (x, y - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(frame, last_suggestion, (10, frame.shape[0] - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Show the output
    cv2.imshow("Emotion Detection", frame)

    # Quit on "q" key press
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
