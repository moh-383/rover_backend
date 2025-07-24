from fastapi import APIRouter
from models.schemas import GPSData
from state import rover_state

router = APIRouter()

@router.post("/")
def update_gps(data: GPSData):
    rover_state["gps"] = data
    return {"message": "Coordonnées GPS mises à jour"}

@router.get("/")
def get_gps():
    return rover_state.get("gps")
