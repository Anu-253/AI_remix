# 🎵 AI Music Remix & Mood Generator

An AI-powered music remix application that analyzes songs based on mood and generates remixed audio outputs accordingly. The system allows users to select songs from a predefined library and apply mood-based remix transformations.

---

## 📌 Problem Statement

Traditional music remixing requires technical knowledge of audio processing tools and music production software. Most students and non-professionals lack the expertise to remix music or adapt songs based on emotional moods. Existing music applications mainly focus on playback and recommendation rather than creative remix generation.

---

## 💡 Proposed Solution

This project presents a web-based AI music remix system that:
- Analyzes audio tracks using machine learning
- Predicts the emotional mood of a song
- Applies remix transformations based on the predicted mood
- Allows users to listen to and download remixed versions

---

## 🧠 System Architecture

**Modules:**
- **Frontend:** User interface for song selection and remix playback  
- **Backend:** Handles audio processing and model inference  
- **Machine Learning Model:** Mood classification using audio features  
- **Database:** Stores song metadata and file paths  

---

## ⚙️ Technologies Used

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn (Random Forest Classifier)  
- **Audio Processing:** Librosa, SoundFile  
- **Web Framework:** Streamlit  
- **Database:** SQLite  
- **Model Persistence:** Joblib  

---

## 🧪 Machine Learning Details

### Feature Extraction
The following audio features are extracted:
- Tempo
- RMS Energy
- Spectral Centroid
- Zero Crossing Rate

### Model
- Random Forest Classifier
- Trained on ~80 audio samples across four moods:
  - Happy
  - Calm
  - Sad
  - Energy

### Performance
- **Accuracy:** 76%
- **Weighted F1-score:** 0.76

---

## 🔁 Workflow

1. User selects a song from the library
2. Audio features are extracted
3. ML model predicts the song’s mood
4. Remix logic is applied based on mood
5. Remixed audio is generated and played
6. User can download the remixed song

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Anu-253/AI_remix.git
cd AI_remix
2️⃣ Install dependencies


pip install -r requirements.txt
3️⃣ Train the model 


python model/train_mood_classifier.py
4️⃣ Ingest songs into database


python ingest_songs.py
5️⃣ Run the application


streamlit run app/app1/app.py
📈 Future Scope
Expand dataset with more genres and languages (Bollywood, English, etc.)

Improve mood classification with deep learning models

Add advanced remix features such as beat matching and vocal separation

Deploy as a full-scale cloud-based web or mobile application

📚 References
Librosa Documentation: https://librosa.org

Scikit-learn Documentation: https://scikit-learn.org

DEAM Dataset (Dynamic Emotion in Music)

Research papers on Music Emotion Recognition

👤 Author
Anagha
AI & Web Development Enthusiast


