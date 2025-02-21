# 📥 Installation Guide for Emotion Detector AIML

## 📌 Prerequisites
Before running the project, ensure your system meets the following requirements:

### 🖥️ System Requirements
- Operating System: Windows / macOS / Linux
- Python Version: 3.7 or higher
- Webcam for real-time face detection

### 📦 Required Libraries
Make sure you have the following libraries installed:
- OpenCV (`opencv-python`)
- NumPy
- pyttsx3 (for text-to-speech)
- DeepFace (for emotion detection)

## 🚀 Installation Steps

### 1️⃣ Clone the Repository
First, clone the repository from GitHub:
```bash
git clone https://github.com/debanganghosh08/emotion_detector_AIML.git
```
Move into the project directory:
```bash
cd emotion_detector_AIML
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
To avoid package conflicts, create a virtual environment:
```bash
python -m venv env
```
Activate the virtual environment:
- **Windows:**
  ```bash
  env\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source env/bin/activate
  ```

### 3️⃣ Install Dependencies
Run the following command to install all necessary dependencies:
```bash
pip install -r requirements.txt
```
If you don’t have a `requirements.txt` file, manually install the required packages:
```bash
pip install opencv-python numpy pyttsx3 deepface
```

### 4️⃣ Run the Project
Once the installation is complete, start the emotion detection system:
```bash
python emotion_ai.py
```

## 🎯 Usage Instructions
- Press **'P'** to analyze and predict emotions.
- Press **'Q'** to exit the application.

## ❓ Troubleshooting
- **ModuleNotFoundError:** Run `pip install <missing_module>` to install the required module.
- **Permission Denied Error:** Run the script with administrator privileges.
- **Webcam Issues:** Ensure your webcam is properly connected and accessible.

## 📬 Support
For any issues, open an issue on GitHub: [Emotion Detector AIML](https://github.com/debanganghosh08/emotion_detector_AIML/issues)

🚀 Happy Coding! 🎭

