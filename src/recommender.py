import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

# Emotion → keywords in multiple languages
EMOTION_MUSIC_MAP = {
    "joy": [
        "happy upbeat english",
        "happy songs tamil",
        "happy songs malayalam",
        "happy songs hindi",
        "happy songs telugu",
    ],
    "sadness": [
        "sad songs english",
        "sad songs tamil",
        "sad songs malayalam",
        "sad songs hindi",
        "sad songs telugu",
    ],
    "anger": [
        "angry intense english",
        "angry songs tamil",
        "angry songs malayalam",
        "angry songs hindi",
        "angry songs telugu",
    ],
    "fear": [
        "calming peaceful english",
        "soothing songs tamil",
        "soothing songs malayalam",
        "soothing songs hindi",
        "soothing songs telugu",
    ],
    "surprise": [
        "exciting upbeat english",
        "energetic songs tamil",
        "energetic songs malayalam",
        "energetic songs hindi",
        "energetic songs telugu",
    ],
    "disgust": [
        "moody dark english",
        "moody songs tamil",
        "moody songs malayalam",
        "moody songs hindi",
        "moody songs telugu",
    ],
    "neutral": [
        "chill lofi english",
        "chill songs tamil",
        "chill songs malayalam",
        "chill songs hindi",
        "chill songs telugu",
    ],
}

def get_recommendations(emotion, limit=2):
    keywords = EMOTION_MUSIC_MAP.get(emotion, EMOTION_MUSIC_MAP["neutral"])
    
    tracks = []
    seen = set()  # avoid duplicates

    for keyword in keywords:
        results = sp.search(q=keyword, type="track", limit=limit)
        for track in results["tracks"]["items"]:
            track_id = track["id"]
            if track_id not in seen:
                seen.add(track_id)
                tracks.append({
                    "name": track["name"],
                    "artist": track["artists"][0]["name"],
                    "url": track["external_urls"]["spotify"],
                    "image": track["album"]["images"][0]["url"] if track["album"]["images"] else None,
                    "preview": track.get("preview_url", None)
                })
    return tracks

if __name__ == "__main__":
    print("Testing multilingual recommendations for JOY...\n")
    tracks = get_recommendations("joy")
    for t in tracks:
        print(f"🎵 {t['name']} — {t['artist']}")
        print(f"   🔗 {t['url']}\n")