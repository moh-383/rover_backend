from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import sensors, map, control

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sensors.router, prefix="/sensors")
app.include_router(map.router, prefix="/map")
app.include_router(control.router, prefix="/control")

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur le backend du Rover"}
