from dataclasses import dataclass
from models.Exam import Exam


@dataclass
class Patient:
    id: int
    name: str
    surname: str
    image: str
    exam_history: list[Exam]
