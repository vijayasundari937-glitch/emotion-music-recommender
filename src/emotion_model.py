from transformers import pipeline
from deep_translator import GoogleTranslator

print("Loading multilingual emotion model...")
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)

def detect_emotion(text):
    try:
        translated = GoogleTranslator(source="auto", target="en").translate(text)
        print(f"   (Translated: '{translated}')")
    except:
        translated = text

    result = emotion_classifier(translated)
    emotion = result[0][0]["label"].lower()
    score = round(result[0][0]["score"] * 100, 2)
    return emotion, score

if __name__ == "__main__":
    test_sentences = [
        "I am so happy today!",
        "நான் மிகவும் சந்தோஷமாக இருக்கிறேன்",
        "എനിക്ക് വളരെ സന്തോഷം ഉണ്ട്",
        "मुझे बहुत दुख है",
        "Estoy muy enojado",
    ]

    for sentence in test_sentences:
        print(f"📝 '{sentence}'")
        emotion, confidence = detect_emotion(sentence)
        print(f"   → Emotion: {emotion} ({confidence}% confidence)\n")