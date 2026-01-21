import librosa
import soundfile as sf
import os

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def remix_audio(input_path, mood):
    y, sr = librosa.load(input_path, sr=None, mono=True)

    if mood == "calm":
        y = librosa.effects.time_stretch(y, rate=0.9)

    elif mood == "sad":
        y = librosa.effects.pitch_shift(y, sr=sr, n_steps=-3)

    elif mood == "happy":
        y = librosa.effects.time_stretch(y, rate=1.05)
        y = y * 1.1

    elif mood == "energy":
        y = y * 1.25

    y = librosa.util.normalize(y)

    output_path = os.path.join(
        OUTPUT_DIR,
        f"remix_{os.path.basename(input_path)}"
    )

    sf.write(output_path, y, sr)
    return output_path
