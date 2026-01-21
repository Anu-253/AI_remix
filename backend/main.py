from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

from audio_utils import extract_features, predict_mood, remix_audio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class RemixRequest(BaseModel):
    song_path: str | None = None   # 👈 IMPORTANT

@app.post("/remix")
def remix(request: RemixRequest):
    song_path = request.song_path or "test.mp3"  # 👈 fallback

    print("👉 Received song_path:", song_path)

    if not os.path.exists(song_path):
        return {
            "detected_mood": "Unknown",
            "error": "Song file not found"
        }

    tempo, energy, centroid = extract_features(song_path)
    mood = predict_mood(tempo, energy, centroid)

    os.makedirs("output", exist_ok=True)
    output_path = "output/remixed.wav"

    remix_audio(song_path, mood, output_path)

    print("🎶 Remix done, mood:", mood)

    return {
        "detected_mood": mood,
        "output_path": output_path
    }
