from dataclasses import dataclass
from models.Exam import Exam

@dataclass
class User:
    id: int
    name: str
    surname: str
    image: str
    login: str
    password: str
