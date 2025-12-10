from enum import Enum


class Command(Enum):
    HELP = "help"
    SHOW = "show"
    NEXT = "next"
    JUMP = "jump"
    PREV = "prev"
    CREATE = "create"
