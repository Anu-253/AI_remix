import os
import librosa
import numpy as np
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


# -----------------------------
# 1. Feature extraction
# -----------------------------
def extract_features(audio_path):
    y, sr = librosa.load(audio_path, duration=30)

    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    
    tempo = float(tempo)

    rms = np.mean(librosa.feature.rms(y=y))
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))

    return [tempo, rms, spectral_centroid, zcr]


# -----------------------------
# 2. Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# (We load DEAM only to show dataset usage — not for training here)
deam_path = os.path.join(BASE_DIR, "..", "data", "deam_with_moods.csv")
df = pd.read_csv(deam_path)

print("✅ DEAM dataset loaded successfully")
print("Available columns:", list(df.columns))


# -----------------------------
# 3. Load audio samples (THIS is your training data)
# -----------------------------
audio_base = os.path.join(BASE_DIR, "..", "dataset", "songs")

X = []
y = []

for mood in os.listdir(audio_base):
    mood_folder = os.path.join(audio_base, mood)

    if not os.path.isdir(mood_folder):
        continue

    for file in os.listdir(mood_folder):
        if file.endswith(".wav") or file.endswith(".mp3"):
            path = os.path.join(mood_folder, file)
            features = extract_features(path)

            X.append(features)
            y.append(mood)   # label = folder name


X = np.array(X)
y = np.array(y)


# -----------------------------
# 4. Train ML model
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# -----------------------------
# 5. Evaluate
# -----------------------------
y_pred = model.predict(X_test)
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))


# -----------------------------
# 6. Save model
# -----------------------------
model_path = os.path.join(BASE_DIR, "mood_classifier.pkl")
joblib.dump(model, model_path)

print(f"\n✅ Model saved successfully at: {model_path}")
