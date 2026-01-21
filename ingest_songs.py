import os
import sqlite3

# -----------------------------
# 1. Database setup
# -----------------------------
DB_NAME = "songs.db"
SONGS_DIR = "dataset/songs"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Create table (runs only once)
cursor.execute("""
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    mood TEXT,
    file_path TEXT
)
""")

conn.commit()

# -----------------------------
# 2. Scan folders & insert songs
# -----------------------------
inserted = 0

for mood in os.listdir(SONGS_DIR):
    mood_folder = os.path.join(SONGS_DIR, mood)

    if not os.path.isdir(mood_folder):
        continue

    for file in os.listdir(mood_folder):
        if file.endswith(".mp3") or file.endswith(".wav"):
            file_path = os.path.join(mood_folder, file)

            cursor.execute(
                "INSERT INTO songs (title, mood, file_path) VALUES (?, ?, ?)",
                (file, mood, file_path)
            )

            inserted += 1

conn.commit()
conn.close()

print(f"✅ Successfully ingested {inserted} songs into the database.")
