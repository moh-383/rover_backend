from pydantic import BaseModel

class MoveCommand(BaseModel):
    direction: str  # "forward", "backward", "left", "right", "stop"