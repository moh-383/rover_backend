# app/routers/sensors.py

from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.services.detection import detect_mine

router = APIRouter()

# ✅ Structure des données capteurs envoyées par Arduino
class SensorData(BaseModel):
    temperature: float
    humidity: float
    gas: int
    distance: int
    magnetic_field: int
    metal: int
    battery: int
    altitude: float
    pressure: float
    tension: float

@router.post("/data")
async def receive_sensor_data(sensor_data: SensorData):
    data_dict = sensor_data.dict()

    # Exécuter la logique de détection
    detection_result = detect_mine(data_dict)

    # Réponse complète pour Flutter
    return {
        "detection": detection_result,
        "battery": f"{sensor_data.battery}%",
        "temperature": f"{sensor_data.temperature}°C",
        "humidity": f"{sensor_data.humidity}%",
        "distance": f"{sensor_data.distance} cm",
        "altitude": f"{sensor_data.altitude} m",
        "pressure": f"{sensor_data.pressure} hPa",
        "tension": f"{sensor_data.tension} V"
    }
