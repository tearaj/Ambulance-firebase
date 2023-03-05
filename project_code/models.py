from enum import Enum
class signal_value(str, Enum):
    stop = "Stop"
    wait = "Wait"
    straight = "Straight"
    right = "Right"
    left = "Left"
    u_turn = "U-Turn"
