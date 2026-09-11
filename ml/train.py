import json
from pathlib import Path


import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "training_intents.json"
MODEL_DIR = BASE_DIR / "ml" / "model"

MODEL_DIR.mkdir(parents=True, exist_ok=True)
# Load training data 

def load_training_data(path: Path) -> tuple[list[str], list[str]]:
    """Ucitava JSON {intent: [primjeri]} i vraca (texts, labels)."""
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)

    texts: list[str] = []
    labels: list[str] = []
    for intent, examples in raw.items():
        for example in examples:
            texts.append(example)
            labels.append(intent)

    return texts, labels
#categorizing the data into texts and labels for learning

def train_model(texts: list[str], labels: list[str]):
    """Pretvara tekst u TF-IDF vektore i trenira Logistic Regression klasifikator."""
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression()
    model.fit(X, labels)

    return model, vectorizer

def main():
    texts, labels = load_training_data(DATA_PATH)
    print(f"Ucitano {len(texts)} primjera u {len(set(labels))} kategorija.")

    model, vectorizer = train_model(texts, labels)

    joblib.dump(model, MODEL_DIR / "intent_model.pkl")
    joblib.dump(vectorizer, MODEL_DIR / "vectorizer.pkl")

    print(f"Model sacuvan u {MODEL_DIR}")


if __name__ == "__main__":
    main()