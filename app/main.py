from fastapi import FastAPI
import json
from fastapi.responses import JSONResponse

app = FastAPI(title="Personen-API", description="Verwaltung einfacher Personendaten")

# Daten aus JSON laden
with open("app/data.json", "r", encoding="utf-8") as f:
    personen = json.load(f)

@app.get("/personen")
def list_personen():
    return list(personen.keys())

@app.get("/")
def startseite():
    return {"info": "Willkommen bei der Personen-API. Bitte /personen aufrufen."}