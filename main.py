from aiogram import executor, Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = "7719840273:AAEg-OpBFBo7PUplIy0d6B9iP5LzKPqS2qo"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def all_massages(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def start(message):
   print('Введите команду /start, чтобы начать общение.')



if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)