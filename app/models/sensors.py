from pydantic import BaseModel

class SensorData(BaseModel):
    temperature: float         # En °C
    magnetic_field: float      # En Tesla simulé
    ir_detected: bool          # Objet détecté ou non
