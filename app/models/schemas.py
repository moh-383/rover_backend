from pydantic import BaseModel

class SensorData(BaseModel):
    temperature: float
    magnetic_field: float
    gas: float
    distance: float
    metal: float
    ir_detected: bool

class GPSData(BaseModel):
    latitude: float
    longitude: float

class MoveCommand(BaseModel):
    direction: str  # "forward", "backward", "left", "right", "stop"
