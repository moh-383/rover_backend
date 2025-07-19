from fastapi import FastAPI
from app.routers import control,sensors

app = FastAPI()

# On ajoute le router de pilotage du rover
app.include_router(control.router, prefix="/control", tags=["Control"])
# On ajoute le router de données capteurs
app.include_router(sensors.router, prefix="/sensors", tags=["Sensors"])