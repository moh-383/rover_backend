from fastapi import APIRouter
from app.models.sensors import SensorData
import random

router = APIRouter()

@router.get("/", response_model=SensorData)
def get_sensor_data():
    # Simulation de données capteurs
    return SensorData(
        temperature=round(random.uniform(20.0, 40.0), 2),
        magnetic_field=round(random.uniform(0.1, 0.9), 2),
        ir_detected=random.choice([True, False])
    )
