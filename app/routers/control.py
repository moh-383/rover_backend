from fastapi import APIRouter
from models.schemas import MoveCommand
from state import rover_state

router = APIRouter()

@router.post("/")
def control_rover(cmd: MoveCommand):
    rover_state["movement"] = cmd
    return {"message": f"Mouvement: {cmd.direction}"}

@router.get("/")
def get_last_command():
    return rover_state.get("movement")
