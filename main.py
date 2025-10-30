import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards import get_start_kb, get_inline_kb

bot = Bot(token="8276962154:AAEB_f2WnImnxVThwE3VMjKX4_noqn6aXG4")
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    # Одно сообщение одна клавиатура
    await message.answer("Привет я шутник", reply_markup=get_start_kb())

@dp.message(F.text == "Кнопка1")
async def button1_handler(message: Message):
    await message.answer_photo(
        "https://pochemychki.com.ua/wp-content/uploads/2024/11/6-1-1.webp",
        caption="Чихуахуа"
    )

@dp.message(F.location)
async def location_handler(message: Message):
    await message.answer(
        f"{message.location.latitude}, {message.location.longitude}",
    )
@dp.message(F.contact)
async def location_handler(message: Message):
    await message.answer(
        f"{message.contact.first_name}\n{message.contact.last_name if message.contact.last_name else 'ХХХ'}\n{message.contact.phone_number}",
    )

@dp.message(F.text == "Обычная Кнопка")
async def button_handler(message: Message):
    await message.answer("Чек", reply_markup=ReplyKeyboardRemove())
    await message.answer("Выберите Действие", reply_markup=get_inline_kb())

@dp.callback_query(F.data == "jaxangir")
async def cb_handler(cb: CallbackQuery):
    print(cb)
    print(cb.message.text)
    print(cb.data)
    await cb.answer("Привет")
    await cb.message.answer("Hello")

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
