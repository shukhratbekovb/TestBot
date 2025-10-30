import asyncio
from pyexpat.errors import messages

from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards import get_start_kb, get_inline_kb, get_test_kb

bot = Bot(token="8276962154:AAEB_f2WnImnxVThwE3VMjKX4_noqn6aXG4")
dp = Dispatcher()
data = {}
@dp.message(CommandStart())
async def start_handler(message: Message):
    # Одно сообщение одна клавиатура
    data.clear()
    await message.answer("В каком году вторая мировая\nA)1940\nB)1941\nC)1939\nD)1938", reply_markup=get_test_kb(1))

@dp.callback_query(F.data.startswith("test"))
async def test_handler(cb: CallbackQuery):
    _, number, answer = cb.data.split("_")
    print(cb.data)
    data[number] = answer  # { "1": "A"}
    if number == "1":
        await cb.message.edit_text(
            "В каком году закончилась 2 мировая? A B C D",
            reply_markup=get_test_kb(2)
        )
    elif number == "2":
        await cb.message.edit_text(
            "Вы прошли Тест",
            reply_markup=None
        )
        await cb.message.answer(f"{data}")



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())