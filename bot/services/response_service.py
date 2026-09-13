import json 
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
RESPONSE_PATH = BASE_DIR / "data" / "restaurant_info.json"

with open(RESPONSE_PATH,encoding="utf-8") as f:
    RESPONSES = json.load(f)

def get_response(intent:str) -> str:
    #ova funkcija nas osigurava da ako nemamo adekvatan odgovor necemo dati neku glupost
    return RESPONSES.get(intent,"Izvini ne znam kako da odgovorim na to pitannje")



if __name__ == "__main__":
    import sys
    sys.path.append(str(BASE_DIR / "ml"))
    from predict import predict_intent

    test_pitanja = [
        "da li radite subotom",
        "imate li oradu",
        "koliko kosta vecera",
        "gdje ste smjesteni",
    ]

    for pitanje in test_pitanja:
        intent = predict_intent(pitanje)
        odgovor = get_response(intent)
        print(f"Pitanje: {pitanje}")
        print(f"Prepoznata kategorija: {intent}")
        print(f"Odgovor: {odgovor}")
        print("---")