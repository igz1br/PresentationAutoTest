from fastapi import FastAPI
from app.mocks import QuestionModel, Question

app = FastAPI()  # noqa: pylint=invalid-name

question_model = QuestionModel()

@app.get(path="/question/")
async def question(*, ques_id: int = None):
    result = question_model.get(ques_id)
    return result

@app.post("/release/")
async def release(*, chat_id: int = None):
    if chat_id//10 > 10:
        return chat_id**2
    else:
        return chat_id**-2
    

