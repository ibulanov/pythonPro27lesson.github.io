from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram.utils.markdown import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import datetime
from aiogram.dispatcher import filters

bot = Bot(token="7579456182:AAGSVyJ0B_Yw98qwGTLVvsELTYNafdyB1jE")
dp = Dispatcher(bot)

web_app = WebAppInfo(url="https://ibulanov.github.io/pythonPro27lesson.github.io/")
kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(KeyboardButton(text="site", web_app=web_app))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Это магазин продуктов", reply_markup=kb_main)

buy_kb = ReplyKeyboardMarkup(resize_keyboard=True)
buy_kb.add(KeyboardButton("Оплатить"))
price = 0

@dp.message_handler(content_types="web_app_data")
async def get_data(web_app_message):
    global price
    begin = web_app_message.web_app_data.data.rfind(" ")
    end = web_app_message.web_app_data.data.rfind("$")
    price = web_app_message.web_app_data.data[begin + 1:end]
    await bot.send_message(web_app_message.chat.id,
                           web_app_message.web_app_data.data, reply_markup=buy_kb)

@dp.message_handler(filters.Text(contains="Оплатить"))
async def buy(message: types.Message):
    await message.answer(f"Спасибо за покупку на {price}$")

executor.start_polling(dp, skip_updates=True)
