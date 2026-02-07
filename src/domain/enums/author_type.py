from enum import Enum


class AuthorType(str, Enum):
    PERSON = "person"
    GROUP = "group"
