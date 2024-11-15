from aiogram import executor, Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio



api = ""
bot = Bot(token=api)

dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup( resize_keyboard=True, one_time_keyboard=True)
botum = KeyboardButton(text='Рассчитать', resize_keyboard="100x100")
botum2 = KeyboardButton(text='Информация', resize_keyboard="100x100")
kb.row(botum, botum2)

class UserState(StatesGroup):
     age = State()
     growth = State()
     weight = State()

@dp.message_handler(commands=['start'])
async def all_massages(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)

@dp.message_handler(text="Рассчитать")
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(qw=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(qw1=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(qw2=message.text)
    a = await state.get_data()
    i = 10*int(a['qw2']) + 6.25*int(a['qw1']) + 5 - 5*int(a['qw'])
    await message.answer(f"Ваша норма каллорий {i}")
    await state.finish()

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
