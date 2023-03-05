from enum import Enum
import pydantic
class colors(str, Enum):
    red = "Red"
    yellow = "Yellow"
    green = "Green"
