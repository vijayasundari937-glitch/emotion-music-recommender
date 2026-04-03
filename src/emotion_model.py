from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

# Load pre-trained emotion detection model
print("Loading emotion model... (first time may take a minute)")
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)

def detect_emotion(text):
    result = emotion_classifier(text)
    emotion = result[0][0]["label"].lower()
    score = round(result[0][0]["score"] * 100, 2)
    return emotion, score

# Test it
if __name__ == "__main__":
    test_sentences = [
        "I just got promoted at work!",
        "I feel so lonely and sad today",
        "I am so angry right now",
        "feeling peaceful and calm",
        "I'm scared about the future"
    ]
    
    for sentence in test_sentences:
        emotion, confidence = detect_emotion(sentence)
        print(f"📝 '{sentence}'")
        print(f"   → Emotion: {emotion} ({confidence}% confidence)\n")