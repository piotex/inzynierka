from dataclasses import dataclass


@dataclass
class Exam:
    id: int
    image: str
    result: str
    date: str

    def get_dict(self):
        return {
            "id": self.id,
            "image": self.image,
            "result": self.result,
            "date": self.date,
        }

