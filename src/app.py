import streamlit as st
from emotion_model import detect_emotion
from recommender import get_recommendations

# Page config
st.set_page_config(
    page_title="Emotion Music Recommender",
    page_icon="🎵",
    layout="centered"
)

# Header
st.title("🎵 Emotion-Aware Music Recommender")
st.markdown("Tell me how you feel and I'll find the perfect songs for you.")
st.divider()

# Emotion icons
EMOTION_ICONS = {
    "joy":      "😄",
    "sadness":  "😢",
    "anger":    "😡",
    "fear":     "😨",
    "surprise": "😲",
    "disgust":  "🤢",
    "neutral":  "😐"
}

# Input
user_input = st.text_area(
    "How are you feeling right now?",
    placeholder="e.g. I just got promoted! / I feel really lonely today...",
    height=100
)

if st.button("🎧 Find My Music", use_container_width=True):
    if user_input.strip() == "":
        st.warning("Please type something about how you feel!")
    else:
        with st.spinner("Detecting your emotion..."):
            emotion, confidence = detect_emotion(user_input)

        icon = EMOTION_ICONS.get(emotion, "🎭")
        st.success(f"{icon} Detected emotion: **{emotion.capitalize()}** ({confidence}% confidence)")
        st.divider()

        with st.spinner("Finding your songs..."):
            tracks = get_recommendations(emotion, limit=6)

        st.subheader(f"🎶 Songs for your {emotion} mood")

        for i, track in enumerate(tracks):
            col1, col2 = st.columns([1, 3])
            with col1:
                if track["image"]:
                    st.image(track["image"], width=80)
            with col2:
                st.markdown(f"**{track['name']}**")
                st.markdown(f"*{track['artist']}*")
                st.markdown(f"[Open in Spotify ↗]({track['url']})")
            st.divider()