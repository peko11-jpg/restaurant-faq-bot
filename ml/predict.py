from pathlib import Path

import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "ml" / "model"

model = joblib.load(MODEL_DIR / "intent_model.pkl")
vectorizer = joblib.load(MODEL_DIR / "vectorizer.pkl")

def predict_intent(text: str) -> str:
    """Vraca predvidjenu kategoriju za dato pitanje."""
    X = vectorizer.transform([text])
    prediction = model.predict(X)
    return prediction[0]

if __name__ == "__main__":
    test_pitanja = [
        "da li radite subotom",
        "imate li oradu",
        "u koliko sati zatvarate",
    ]

    for pitanje in test_pitanja:
        kategorija = predict_intent(pitanje)
        print(f"'{pitanje}' -> {kategorija}")