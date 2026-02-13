# 🎵 Music Mashup Generator

A Python-based web application that automatically generates a music mashup from YouTube songs of a selected singer.

## 🚀 Live Demo

👉 **Try the app here:**
https://mashup-project-tmy3bfvhz7wfpqqxmdn98n.streamlit.app/

## 📌 Features

* Download songs from YouTube automatically
* Extract first *N seconds* from each track
* Merge audio clips into a single mashup
* Web interface built with Streamlit
* Instant audio playback in browser

## 🛠️ Technologies Used

* Python
* Streamlit
* yt-dlp (YouTube downloader)
* MoviePy (audio processing)
* Pydub (audio merging)
* FFmpeg

## ▶️ How to Run Locally

1. Clone the repository:

   ```
   git clone https://github.com/Anshi2611/mashup-project.git
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the app:

   ```
   streamlit run app.py
   ```

## 📂 Project Structure

```
mashup-project/
│
├── app.py              # Streamlit web app
├── 102303605.py        # Mashup generator script
├── requirements.txt
└── downloads/
```

## 🎯 Author

**Anshika Gupta**

---

✨ This project was developed as part of a programming assignment to demonstrate automation, multimedia processing, and web deployment using Python.
