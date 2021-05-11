from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2
    BLACK = 3

e = Color.RED.value
print(e)