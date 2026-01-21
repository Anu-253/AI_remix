import streamlit as st
from backend.audio_utils import remix_audio
from song_links import SONGS

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Music Remix",
    page_icon="🎧",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("🎧 AI Music Remix & Mood Generator")
st.caption("Local demo · Mood-based audio remixing")
st.divider()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎵 Library")
category = st.sidebar.radio("Select category", list(SONGS.keys()))

# ---------------- SEARCH ----------------
search_query = st.text_input(
    "🔍 Search songs",
    placeholder="Type song name..."
).lower()

MOODS = ["happy", "sad", "calm", "energy"]
songs = SONGS[category]

# ---------------- SONG LIST ----------------
for song_name, song_data in songs.items():
    if search_query and search_query not in song_name.lower():
        continue

    song_path = song_data["path"]
    cover_path = song_data["cover"]

    with st.container():
        col_img, col_main = st.columns([1, 5], vertical_alignment="center")

        with col_img:
            st.image(cover_path, use_container_width=True)

        with col_main:
            st.subheader(song_name)
            st.caption("Preview clip · Select mood and remix")

            col_audio, col_mood, col_btn = st.columns([3, 1, 1])

            with col_audio:
                st.audio(song_path)

            with col_mood:
                mood = st.selectbox(
                    "Mood",
                    MOODS,
                    key=f"mood_{song_name}"
                )

            with col_btn:
                if st.button("Remix", key=f"remix_{song_name}"):
                    with st.spinner("Remixing audio..."):
                        out = remix_audio(song_path, mood)

                    st.success(f"Remixed as {mood}")
                    st.audio(out)

                    with open(out, "rb") as f:
                        st.download_button(
                            "⬇️ Download Remix",
                            data=f,
                            file_name=f"{song_name}_{mood}_remix.wav",
                            mime="audio/wav"
                        )

        st.divider()
