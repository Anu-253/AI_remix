# 🎵 AI Music Remix & Mood Generator

An AI-powered music remix application that classifies song mood using machine learning and automatically applies mood-based remix transformations.

Built with Python, Streamlit, Librosa, and Scikit-learn.

## 🚀 Features

* Upload or select songs from a predefined library
* Extract audio features using Librosa
* Predict song mood using a Random Forest classifier
* Generate mood-based remixed audio
* Play and download remixed tracks through a web interface

---

## 🛠 Tech Stack

**Frontend**

* Streamlit

**Machine Learning**

* Scikit-learn
* Random Forest Classifier

**Audio Processing**

* Librosa
* SoundFile

**Database**

* SQLite

**Utilities**

* Joblib
* NumPy
* Pandas

---

## 🧠 Machine Learning Pipeline

### Feature Extraction

The model extracts audio features including:

* Tempo
* RMS Energy
* Spectral Centroid
* Zero Crossing Rate

### Mood Classes

* Happy
* Calm
* Sad
* Energetic

### Performance

* Accuracy: **76%**
* Weighted F1 Score: **0.76**

---

## 🔄 Workflow

1. User selects a song
2. Audio features are extracted
3. ML model predicts song mood
4. Mood-specific remix transformations are applied
5. Remixed audio is generated
6. User can listen to or download the output

---

## 📂 Project Structure

```bash
AI_remix/
│
├── app/
├── model/
├── database/
├── ingest_songs.py
├── requirements.txt
└── README.md
```

---

## ⚡ Installation

```bash
git clone https://github.com/Anu-253/AI_remix.git
cd AI_remix
pip install -r requirements.txt
```

### Train Model

```bash
python model/train_mood_classifier.py
```

### Populate Database

```bash
python ingest_songs.py
```

### Run Application

```bash
streamlit run app/app1/app.py
```

---

## 📈 Future Improvements

* Deep learning-based mood classification
* Larger multi-language music datasets
* Beat synchronization and vocal separation
* Cloud deployment for real-time remix generation

---

## 👩‍💻 Author

**Anagha P Kulkarni**

AI/ML Engineer • Full-Stack Developer

GitHub: https://github.com/Anu-253
