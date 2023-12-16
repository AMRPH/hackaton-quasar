import asyncio
import logging
import sys

from decouple import config
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
import asyncio

import sys
sys.path.append('../hackaton-llm')

from model.model import Quasar
from model.API_KEY import API_KEY


bot = Bot(token=config('TOKEN'), parse_mode=ParseMode.HTML)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Здравствуйте, {hbold(message.from_user.full_name)}! Это бот команды Astrum - Quasar. Введите свой вопрос:")


@dp.message()
async def QuasarAnswer(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, 'Ожидайте, ответ обрабатывается...')
    quasar = Quasar(API_KEY=API_KEY)
    response = quasar.answer(message.text)
    await message.answer(f'<b>Ответ:</b> {response[0]}\n<b>НПА:</b> {response[1]}\n<b>Ссылка:</b> {response[2]}\n<i>*Ссылка может быть не достоверной</i>', parse_mode=ParseMode.HTML)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())