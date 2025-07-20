from fastapi import APIRouter
import serial

router = APIRouter()
ser = serial.Serial('/dev/ttyUSB1', 9600)  # GPS séparé du pilotage

@router.get("/")
def get_gps():
    line = ser.readline().decode().strip()
    try:
        lat, lon, angle = map(float, line.split(","))
        return {"lat": lat, "lon": lon, "angle": angle}
    except:
        return {"error": "Invalid GPS data"}
