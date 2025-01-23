from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



Yes_no = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="✅ Да"),
                    KeyboardButton(text="❌ Нет"),
                ]
            ],
            resize_keyboard=True,
        )

starts = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Получить данные по товару"),
                ]
            ],
            resize_keyboard=True,
            input_field_placeholder='Получить данные по товару'
        )


