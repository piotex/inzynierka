from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    surname: str
    image: str
    login: str
    password: str
    role: str
