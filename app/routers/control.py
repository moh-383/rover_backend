from fastapi import APIRouter
import serial

router = APIRouter()
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adapter le port

@router.get("/move")
def move_robot(direction: str):
    cmd = {
        "forward": "F",
        "backward": "B",
        "left": "L",
        "right": "R",
        "stop": "S"
    }.get(direction.lower(), "S")
    ser.write(cmd.encode())
    return {"status": "ok", "command": cmd}
