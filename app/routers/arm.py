# app/routers/arm.py

from fastapi import APIRouter
import requests

router = APIRouter()

# Remplace par l'IP réelle de l'ESP32-CAM
ESP32_IP = "http://172.19.218.206"  # à modifier quand tu connais l'IP

@router.post("/start_servo")
async def start_servo():
    try:
        response = requests.get(f"{ESP32_IP}/start_servo")
        return {"message": "Commande envoyée", "esp32_response": response.text}
    except Exception as e:
        return {"error": str(e)}

@router.post("/stop_servo")
async def stop_servo():
    try:
        response = requests.get(f"{ESP32_IP}/stop_servo")
        return {"message": "Commande envoyée", "esp32_response": response.text}
    except Exception as e:
        return {"error": str(e)}
