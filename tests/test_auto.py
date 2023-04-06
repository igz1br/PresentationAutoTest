from app.mocks import QuestionModel, Question
import pytest

test_question_model = QuestionModel()

def test_get():
    test_id = 1
    result = test_question_model.get(id=test_id)
    assert isinstance (result, Question)
    assert result.id == test_id

def test_get_fail():
    test_id = -1
    with pytest.raises(ValueError):
        test_question_model.get(id=test_id)
    
def test_create():
    test_id = 15
    test_question_model.create(id=test_id, text="test", answers=["test list"])
    result = test_question_model.get(id=test_id)
    assert isinstance (result, Question)
    assert result.id == test_id

def test_update():
    test_id = 7
    test_question_model.update(id=test_id, text="new text", answers=["new test list"])
    result = test_question_model.get(id=test_id)
    assert isinstance (result, Question)
    assert result.text == "new text"
    assert isinstance (result.answers, list)
    assert len(result.answers) > 0 
    assert result.answers == ["new test list"]

def test_delete():
    test_id = 5
    test_question_model.delete(id=test_id)
    with pytest.raises(ValueError):
        test_question_model.get(id=test_id)

def test_size_short():
    test_question_model.create(id=100, text="test size", answers=["1", "2"])
    result = test_question_model.size(id=100)
    assert result == "short"
    test_question_model.create(id=101, text="test size", answers=["1", "2", "3"]) #проверка граничных значений
    result = test_question_model.size(id=101)
    assert result == "short"
    test_question_model.create(id=102, text="test size", answers=["1"])
    result = test_question_model.size(id=102)
    assert result == "short"

size_test_data = [
    (4, "medium"),
    (5, "medium"),
    (6, "medium"),
    (7, "long"),
    (8, "long"),
    (100, "long"),
]

@pytest.mark.parametrize("size,expected", size_test_data)
def test_size(size, expected):
    test_answers_list = [str(i) for i in range(size)]
    test_question_model.create(id=200+size, text=f"test #{size}", answers=test_answers_list)
    assert test_question_model.size(id=200+size) == expected , f"error on #{size}"