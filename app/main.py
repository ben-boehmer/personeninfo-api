from fastapi import FastAPI
import json
from fastapi.responses import JSONResponse

app = FastAPI()

with open("app/data.json", "r", encoding="utf-8") as f:
    cities = json.load(f)

@app.get("/cities")
def list_cities():
    return list(cities.keys())

@app.get("/cities/{city_name}")
def get_city(city_name: str):
    city = cities.get(city_name.lower())
    if city:
        return city
    return JSONResponse(status_code=404, content={"error": "City not found"})
