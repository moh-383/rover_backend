# main.py

from fastapi import FastAPI
from app.routers import control, sensors, map

app = FastAPI(
    title="Rover API",
    description="API backend pour le rover détecteur de mines",
    version="1.0.0"
)

app.include_router(control.router, prefix="/control", tags=["Control"])
app.include_router(sensors.router, prefix="/sensors", tags=["Sensors"])
app.include_router(map.router, prefix="/map", tags=["Map"])
