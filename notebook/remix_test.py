import librosa
import soundfile as sf
import os

# ===== CONFIG =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_SONG = os.path.join(
    BASE_DIR,
    "..",
    "dataset",
    "songs",
    "simple-happy-life-353819.mp3"   # 👈 make sure this filename exists
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "..",
    "dataset",
    "songs",
    "output"
)

MOOD = "energetic"   # calm | sad | happy | energetic

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===== LOAD AUDIO =====
y, sr = librosa.load(INPUT_SONG, sr=None, mono=True)
print(f"Loaded audio with sample rate {sr}")

# ===== REMIX FUNCTION =====
def remix_audio(y, sr, mood):
    if mood == "calm":
        y_out = librosa.effects.time_stretch(y, rate=0.7)

    elif mood == "sad":
        y_out = librosa.effects.time_stretch(y, rate=0.7)
        y_out = librosa.effects.pitch_shift(y_out, sr=sr, n_steps=-5)

    elif mood == "happy":
        y_out = librosa.effects.time_stretch(y, rate=1.35)
        y_out = librosa.effects.pitch_shift(y_out, sr=sr, n_steps=3)

    elif mood == "energetic":
        y_out = librosa.effects.time_stretch(y, rate=1.5)
        y_out = librosa.effects.pitch_shift(y_out, sr=sr, n_steps=5)

    else:
        raise ValueError("Invalid mood")

    return librosa.util.normalize(y_out)

# ===== APPLY REMIX =====
y_remix = remix_audio(y, sr, MOOD)

# ===== SAVE OUTPUT =====
base = os.path.splitext(os.path.basename(INPUT_SONG))[0]
output_path = os.path.join(OUTPUT_DIR, f"{base}_{MOOD}.wav")

sf.write(output_path, y_remix, sr)

print(f"Remixed audio saved to: {output_path}")
