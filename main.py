import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command, CommandObject
from aiogram.methods.send_sticker import SendSticker
from aiogram.types.inline_query import InlineQuery
from config_reader import config
from functions import rand_sticker, rand_fem

router = Router()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("rs"))
async def cmd_rs(message: types.Message):
    sticker = rand_sticker()
    await message.reply_sticker(sticker=sticker)

@dp.message(Command("rf"))
async def cmd_rf(message: types.Message, command: CommandObject):
    number = command.args
    response = rand_fem(number)
    await message.reply(response)

@router.inline_query(F.query == "rs")
async def show_user_links(inline_query: InlineQuery):
    sticker = rand_sticker()
    await inline_query.answer_sticker


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
