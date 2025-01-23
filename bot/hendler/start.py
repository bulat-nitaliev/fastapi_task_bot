from aiogram import  types, F
from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.fsm.context import FSMContext
from keyboard.keyboards import  starts
from fetchs.connect import  get_product
from states.state import QuestionData, Questions
from aiogram.types import ReplyKeyboardRemove



start = Router()


#  day
@start.message(F.text=='Получить данные по товару')
async def start_(message:types.Message, state:FSMContext):
    await state.set_state(QuestionData.question) 
    question = Questions()
    await message.answer(question.question,  reply_markup=ReplyKeyboardRemove())


@start.message(QuestionData.question)
async def start1(message:types.Message, state:FSMContext):  
    artikul = message.text
    data = {"artikul": artikul}
    res = await get_product(data=data)
    print(res)
    await state.clear() 
    if 'detail' not in res:
        await message.answer(f'''Ваш результат  
                            \n name - {res['name']}
                            \n articul - {res['articul']}
                            \n price - {res['price']}
                            \n rating - {res['rating']}
                            \n total_quantity - {res['total_quantity']}
                            ''', reply_markup=starts)
    else:
        await message.answer(res['detail'], reply_markup=starts)
    


@start.message(CommandStart)
async def start_bot(message:types.Message):
    data = {
        "username": message.from_user.id,
        "password": message.from_user.id,
        "email": f"user{str(message.from_user.id)}@example.com",
        "first_name": message.from_user.username,
        "last_name": message.from_user.first_name
        }
    # res = await register(data)
    # print(res)
    
    await message.answer('''
        Здравствуйте! 👋\n\n
        Этот бот который по переданному артикулу товара с Wildberries ,\n
        присылает сообщение с самыми свежими данными из бд по этому артикулу,\n
        
        Необходимо  прожать кнопку "Получить данные по товару"
        \n\n
        👇''' , reply_markup=starts)
