from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


# ReplyKeyboardMarkup -> каркас клавиатуры (который меняет основную клав пользователя)
# Он служит чтобы просто упростить ввод текста

# KeyboardButton -> Клавиша Клавиатуры

# kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(
#                 text="Кнопка1"
#             ),
#             KeyboardButton(
#                 text="Кнопка2"
#             )
#         ],
#         [
#             KeyboardButton(
#                 text="Кнопка3"
#             )
#         ]
#     ],
#     resize_keyboard=True
# )
#
# def get_start_kb():
#     return ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(
#                 text="Кнопка1"
#             ),
#             KeyboardButton(
#                 text="Кнопка2"
#             )
#         ],
#         [
#             KeyboardButton(
#                 text="Кнопка3"
#             )
#         ]
#     ],
#     resize_keyboard=True
# )


def get_start_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="Обычная Кнопка"
    )
    builder.button(
        text="Геопозиция",
        request_location=True
    )
    builder.button(
        text="Контакт",
        request_contact=True
    )
    builder.adjust(2, 1)
    return builder.as_markup(
        resize_keyboard=True,
    )


def get_inline_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Ссылка",
        url="https://it911.uz"
    )
    builder.button(
        text="Какая то дата",
        callback_data="jaxangir"
    )
    return builder.as_markup()

def get_test_kb(test_number):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="A",
        callback_data=f"test_{test_number}_A"
    )
    builder.button(
        text="B",
        callback_data=f"test_{test_number}_B"
    )
    builder.button(
        text="C",
        callback_data=f"test_{test_number}_C"
    )
    builder.button(
        text="D",
        callback_data=f"test_{test_number}_D"
    )
    return builder.as_markup()
