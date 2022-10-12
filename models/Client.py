from dataclasses import dataclass
from models.Exam import Exam

@dataclass
class Client:
    id: int
    name: str
    surname: str
    birth_year: int
    image: str
    exam_history: list[Exam]
