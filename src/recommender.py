import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

# Map emotions to search keywords + audio mood
EMOTION_MUSIC_MAP = {
    "joy":      {"keywords": ["happy upbeat", "feel good", "positive vibes"], "energy": "high"},
    "sadness":  {"keywords": ["sad songs", "melancholy", "heartbreak"], "energy": "low"},
    "anger":    {"keywords": ["rage", "intense rock", "aggressive"], "energy": "high"},
    "fear":     {"keywords": ["calming anxiety", "soothing", "peaceful"], "energy": "low"},
    "surprise": {"keywords": ["exciting", "upbeat pop", "energetic"], "energy": "high"},
    "disgust":  {"keywords": ["moody", "dark indie", "alternative"], "energy": "medium"},
    "neutral":  {"keywords": ["chill", "lo-fi", "background music"], "energy": "low"},
}

def get_recommendations(emotion, limit=6):
    mapping = EMOTION_MUSIC_MAP.get(emotion, EMOTION_MUSIC_MAP["neutral"])
    keyword = mapping["keywords"][0]
    
    results = sp.search(q=keyword, type="track", limit=limit)
    
    tracks = []
    for track in results["tracks"]["items"]:
        tracks.append({
            "name": track["name"],
            "artist": track["artists"][0]["name"],
            "url": track["external_urls"]["spotify"],
            "image": track["album"]["images"][0]["url"] if track["album"]["images"] else None,
            "preview": track.get("preview_url", None)
        })
    return tracks

# Test it
if __name__ == "__main__":
    for emotion in ["joy", "sadness", "anger", "fear"]:
        print(f"\n🎭 Emotion: {emotion.upper()}")
        tracks = get_recommendations(emotion, limit=3)
        for t in tracks:
            print(f"  🎵 {t['name']} — {t['artist']}")
            print(f"     🔗 {t['url']}")