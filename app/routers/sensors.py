from fastapi import APIRouter
from app.models.schemas import SensorData
from services.detection import detect_mine
from state import rover_state

router = APIRouter()

@router.post("/")
def receive_sensor_data(data: SensorData):
    rover_state["sensor_data"] = data
    rover_state["mine_status"] = detect_mine(data.dict())
    return {"message": "Données reçues", "mine_status": rover_state["mine_status"]}

@router.get("/")
def get_sensor_data():
    return {
        "sensor_data": rover_state["sensor_data"],
        "mine_status": rover_state["mine_status"]
    }
