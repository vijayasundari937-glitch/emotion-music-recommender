# 🎵 Emotion-Aware Music Recommender

> Tell it how you feel. Get the perfect playlist.

An AI-powered web app that detects the emotion behind your words and recommends Spotify tracks that match your mood — built with a fine-tuned DistilRoBERTa model, Spotify API, and Streamlit.

---

## 🧠 How it works

1. **You type how you feel** — anything from *"I just got promoted!"* to *"feeling lonely tonight"*
2. **AI detects your emotion** — the model classifies your text into one of 7 emotions (joy, sadness, anger, fear, surprise, disgust, neutral)
3. **Emotions map to music mood** — using Spotify's audio features like `valence`, `energy`, and `tempo`
4. **You get a personalised playlist** — real Spotify tracks served instantly with album art and direct links

---

## ✨ Features

- 🔍 DistilRoBERTa model for multi-class emotion classification
- 🎧 Live Spotify track recommendations via Spotify Web API
- 🌈 Covers 7 distinct emotions
- ⚡ Fast, lightweight Streamlit UI — no login required
- 📊 Confidence score shown for each emotion detected
- 🖼️ Album art displayed for every recommended track

---

## 🛠️ Tech stack

| Layer | Technology |
|---|---|
| Emotion model | DistilRoBERTa (HuggingFace Transformers) |
| Music API | Spotify Web API via Spotipy |
| Frontend | Streamlit |
| Data handling | pandas, scikit-learn |
| Environment | Python 3.13+, PyTorch |

---

## 🚀 Getting started

### 1. Clone the repo
```bash
git clone https://github.com/vijayasundari937-glitch/emotion-music-recommender.git
cd emotion-music-recommender
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your Spotify API credentials

Create a free Spotify Developer account at [developer.spotify.com](https://developer.spotify.com), create an app, and copy your credentials.

Create a `.env` file in the root directory:

### 5. Run the app
```bash
cd src
streamlit run app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 📁 Project structure

emotion-music-recommender/
├── data/                   # Raw and processed datasets
├── notebooks/              # Exploratory analysis
├── src/
│   ├── emotion_model.py    # DistilRoBERTa model loading and inference
│   ├── recommender.py      # Spotify API integration and track mapping
│   └── app.py              # Streamlit frontend
├── requirements.txt
├── .env                    # API keys (never commit this)
├── .gitignore
└── README.md

---

## 🎭 Emotion → music mapping

| Detected emotion | Music mood |
|---|---|
| Joy 😄 | Happy, upbeat, feel-good |
| Sadness 😢 | Melancholy, heartbreak, emotional |
| Anger 😡 | Intense, aggressive, rock |
| Fear 😨 | Calming, soothing, peaceful |
| Surprise 😲 | Exciting, energetic, upbeat pop |
| Disgust 🤢 | Moody, dark indie, alternative |
| Neutral 😐 | Chill, lo-fi, background music |

---

## 🔮 Roadmap

- [ ] Selfie-based emotion detection (facial expression input)
- [ ] User accounts and saved playlists
- [ ] Multi-language support
- [ ] Emotion history dashboard
- [ ] Export playlist directly to Spotify

---

## 🙏 Acknowledgements

- [HuggingFace Transformers](https://huggingface.co/transformers)
- [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)
- [Spotipy](https://spotipy.readthedocs.io)
- [Streamlit](https://streamlit.io)

---

## 📄 License

MIT License — feel free to use, modify, and share.

---

<p align="center">Built with 💜 and a lot of feelings</p>