from enum import Enum


class Command(Enum):
    HELP = "help"
    CREATE = "create"
    SHOW = "show"
    UPDATE = "update"
    DELETE = "delete"
    JUMP = "jump"
    NEXT = "next"
    PREV = "prev"
