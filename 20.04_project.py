from aiogram import Bot, types
import random
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.dispatcher import filters
import re

a = ['лазанья', 'жульен', 'карбонара', 'сырный суп', 'пирог']

web_app = WebAppInfo(url="https://ibulanov.github.io/finaltokka.github.io/")
kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(KeyboardButton(text="site", web_app=web_app))

bot = Bot(token="7602865776:AAFgZj1xO8VH4tCrR5O5AdJa7E1RcEx7g9A")
dp = Dispatcher(bot)

buy_kb = ReplyKeyboardMarkup(resize_keyboard=True)
buy_kb.add(KeyboardButton("Оплатить"))

price = 0

@dp.message_handler(commands=['start'])
async def start(mes: types.Message):
    await mes.answer("Хай, это бот кулинар. \n"
                     "Чтобы выдать любой рецепт введите /random_dish \n"
                     "Чтобы посмотреть возможные блюда с вашими продуктами введите /products и выберите из панели нужный продукт",
                     reply_markup=kb_main)

@dp.message_handler(commands=['random_dish'])
async def random_dish(mes: types.Message):
    await mes.answer(random.choice(a))

@dp.message_handler(commands=['products'])
async def products(mes: types.Message):
    await mes.answer('Выбери продукт')

@dp.message_handler(content_types=["web_app_data"])  # ✅ исправлено
async def get_data(web_app_message: types.Message):
    global price
    text = web_app_message.web_app_data.data
    match = re.search(r"С вас (\d+)\$", text)
    if match:
        price = match.group(1)
    else:
        price = "неизвестна"

    await bot.send_message(web_app_message.chat.id, text, reply_markup=buy_kb)

@dp.message_handler(filters.Text(contains="Оплатить"))
async def buy(message: types.Message):
    await message.answer(f"Спасибо за покупку на {price}$")

executor.start_polling(dp, skip_updates=True)
