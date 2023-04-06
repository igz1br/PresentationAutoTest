from typing import Optional
from pydantic import BaseModel

class Question(BaseModel):
    id: int
    text: str
    answers: list[str]

class QuestionModel ():
    id: int
    text: str
    answers: list[str]

    _questions = []

    def __init__(self):
        self._questions = []
        for i in range(0,10):
            new_qeustion = Question(id=i, text="test", answers=["test list"])
            self._questions.append(new_qeustion)

    def get(self, id: int):
        for ques in self._questions:
            if ques.id == id:
                return ques
        raise ValueError # выдаем ошибку

    def create(self, id: int, text: str, answers: list[str]):
        new_qeustion = Question(id=id, text=text, answers=answers)
        self._questions.append(new_qeustion)

    def update(self, id: int, text: Optional[str], answers: Optional[list[str]]):
        for idx, ques in enumerate(self._questions):
            if ques.id == id:
                self._questions.pop(idx)
        new_qeustion = Question(id=id, text=text, answers=answers)
        self._questions.append(new_qeustion)

    def delete(self, id: int):
        for idx, ques in enumerate(self._questions):
            if ques.id == id:
                self._questions.pop(idx)
                return ques
        raise ValueError # выдаем ошибку

    def size(self, id: int):
        ques: Question = self.get(id=id)
        if len(ques.answers) <= 3:
            return "short"
        elif len(ques.answers) <= 6:
            return "medium"
        else:
            return "long"

class PollModel():
    id: int
    name: str
    questions: list[QuestionModel]

    _polls = []