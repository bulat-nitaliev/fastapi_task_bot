from aiogram.fsm.state import StatesGroup, State

class QuestionData(StatesGroup):
    question = State()



class Questions:
    def __init__(self) -> None:
        self.question = 'Введите артикул товара Wildberries'
        
