import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
import asyncio

from bot_token import TOKEN

import sys
sys.path.append('../hackaton-llm')

from model.model import Quasar
from model.API_KEY import API_KEY


# Bot token can be obtained via https://t.me/BotFather
bot = Bot(token=TOKEN)

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Здравствуйте, {hbold(message.from_user.full_name)}! Это бот команды Astrum - Quasar. Введите свой вопрос:")


@dp.message()
async def QuasarAnswer(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, 'Ожидайте, ответ обрабатывается...')
    quasar = Quasar(API_KEY=API_KEY)
    response = quasar.answer(message.text)
    await message.answer(f'<b>Ответ:</b> {response[0]}\n<b>НПА:</b> {response[1]}\n<b>Ссылка:</b> {response[2]}\n*Ссылка может быть не достоверной', parse_mode=ParseMode.HTML)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())