from enum import Enum

dummy_data = {
    "id":1,
    "title":"dummy"
}

class order_by(str,Enum):
    asc = "asc"
    desc = "desc"