from enum import Enum


class CommandDo(Enum):
    TAKEOFF = "takeoff"
    LANDING = "land"
    TURN_RIGHT = "cw"
    TURN_LEFT = "ccw"
    MOVE_ON = "forward"
    MOVE_UP = "up"
    MOVE_DOWN = "down"
    MOVE_LEFT = "left"
    MOVE_RIGHT = "right"
    MOVE_BACK = "back"
    GO_TO_POINT = "go"
    CURVE = "curve"

class CommandRead(Enum):
    SPEED = "speed?"
    BATTERY = "battery?"
    TIME = "time?"
    HEIGHT = "height?"
    TEMPERATURE = "temp?"
    ATTITUDE = "attitude?"
    BAROMETER = "baro?"
    ACCELERATION = "acceleration?"
    TOF = "tof?"
    WIFI = "wifi?"
