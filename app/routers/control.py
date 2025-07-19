from fastapi import APIRouter
from app.models.control import MoveCommand
from app.utils.serial_comm import send_command_to_rover

router = APIRouter()

@router.post("/move")
def move_rover(cmd: MoveCommand):
    send_command_to_rover(cmd.direction)
    return {"status": "moving", "direction": cmd.direction}
