import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import StateFilter
from aiogram.filters.command import Command, CommandObject
from aiogram.methods.send_sticker import SendSticker
from aiogram.types.inline_query import InlineQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from config_reader import config
from functions import rand_sticker, rand_fem, rand_ch, rand_male, add_ch, dice, player, del_ch

router = Router()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

class Valentine(StatesGroup):
    valentine_text = State()
    use_template = State()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("rs"))
async def cmd_rs(message: types.Message, command: CommandObject):
    try:
        number = command.args
        number = number.split(" ", 1)
        print(number[0])
        number = int(number[0])
        for i in range(0, number):
            sticker = rand_sticker()
            print("повторят")
            await message.answer_sticker(sticker=sticker)
            i += 1
    except:
        number = 1
        sticker = rand_sticker()
        await message.reply_sticker(sticker=sticker)

@dp.message(Command("rf"))
async def cmd_rf(message: types.Message, command: CommandObject):
    print('got the female comand')
    try:
        number = command.args
        number = number.split(" ", 1)
        print(number[0])
        number = int(number[0])
    except:
        number = 1
    response = rand_fem(number)
    await message.reply(response)

@dp.message(Command("ch"))
async def cmd_ch(message: types.Message, command: CommandObject):
    print('got the char comand')
    try:
        number = command.args
        number = number.split(" ", 1)
        print(number[0])
        number = int(number[0])
    except:
        number = 1
    response = rand_ch(number)
    await message.reply(response)

@dp.message(Command("rm"))
async def cmd_rm(message: types.Message, command: CommandObject):
    print('got the male comand')
    try:
        number = command.args
        number = number.split(" ", 1)
        print(number[0])
        number = int(number[0])
    except:
        number = 1
    response = rand_male(number)
    await message.reply(response)

@dp.message(Command("add"))
async def cmd_add(message: types.Message, command: CommandObject):
    print('got the addition comand')
    try:
        data = command.args
        data = data.split(" ", 1)
        print(data[0])
        response = add_ch(data[0], data[1])
        await message.reply(response)
    except:
        await message.reply("Ошибка в данных")

@dp.message(Command("delete"))
async def cmd_del(message: types.Message, command: CommandObject):
    print('got the removal comand')
    try:
        data = command.args
        data = data.split(" ", 1)
        print(data[0])
        response = del_ch(data[0])
        await message.reply(response)
    except:
        await message.reply("Ошибка в данных")

@dp.message(Command("add"))
async def cmd_add(message: types.Message, command: CommandObject):
    print('got the addition comand')
    try:
        data = command.args
        data = data.split(" ", 1)
        print(data[0])
        response = del_ch(data[0])
        await message.reply(response)
    except:
        await message.reply("Ошибка в данных")

@dp.message(Command("d"))
async def cmd_d(message: types.Message, command: CommandObject):
    try:
        data = command.args
        data = data.split(" ", 1)
        response = dice(int(data[0]), int(data[1]))
        await message.reply(response)
    except:
        try:
            data = command.args
            data = data.split(" ", 1)
            response = dice(int(data[0]), 1)
            await message.reply(response)
        except:
            response = dice(20, 1)
            await message.reply(response)

@dp.message(Command("rp"))
async def cmd_rp(message: types.Message, command: CommandObject):
    try:
        player_list = []
        data = command.args
        data = data.split(" ", -1)
        number = int(data[0])
        data.pop(0)
        player_list = []
        for i in range(number):
            print (i)
            player_list.append(data[i])
        response = random.choice(player_list)
        await message.reply(response)
    except:
        response = player()
        await message.reply(response)

@dp.message(Command("yn"))
async def cmd_rp(message: types.Message, command: CommandObject):
    yn_list = ["да", "нет"]
    try:
        response = random.choice(yn_list)
        await message.reply(response)
    except:
        response = random.choice(yn_list)
        await message.reply(response)


#Блок под ДСВ и предложку в будущем
@dp.message(Command("valentine"))
async def cmd_valentine(message: types.Message, command: CommandObject, state: FSMContext) -> None:
    await state.set_state(Valentine.valentine_text)
    await message.reply("Отправь валентинку следующим сообщением в том формате, в котором она должна быть опубликована (включая все отступы, переносы и прочее, отредактировать не получится)")


@dp.message(Valentine.valentine_text)
async def process_name(message: types.Message, state: FSMContext) -> None:
    print('got the message itself')
    try:
        try:
            caption_pic = message.caption
        except:
            caption_pic=""
        await bot.download(
            message.photo[-1],
            destination=f"./data/valentine_pic.png"
            )
        image_from_pc = FSInputFile("./data/valentine_pic.png")
        await bot.send_photo(
            chat_id=-1002344636217, 
            photo=image_from_pc, 
            caption=caption_pic) 
    except:
        await state.update_data(valentine_text=message.text)
        print(message.text)
        await state.set_state(Valentine.use_template)
        await bot.send_message(-1002344636217, message.text) 
    

#Отдельные фичи под конкретные фразочки
@dp.message(Command("чмок"))
async def cmd_rs(message: types.Message):
    sticker = rand_sticker()
    await message.reply_sticker(sticker="CAACAgIAAxkBAAKZQ2dYj-6kcV6_yqadB9mI8q4GfDhGAALPZAACKKvBSiGdtv4y5lC5NgQ")

@dp.message(Command("спасибо"))
async def cmd_rs(message: types.Message):
    sticker = rand_sticker()
    await message.reply_sticker(sticker="CAACAgIAAxkBAAKZRWdYkCDGXq4i43dziA77nmPuzpQZAAI5ZwAC4cvASiyZAWvW8-HeNgQ")

@dp.message(Command("плюнула"))
async def cmd_rs(message: types.Message):
    sticker = rand_sticker()
    await message.reply_sticker(sticker="CAACAgIAAxkBAAKZyWdYlu0G1-snPjZWh22sQEMeKThqAALkcAACWbHBSgUhVgSuKnHMNgQ")

@dp.message(Command("женщины"))
async def cmd_rs(message: types.Message):
    sticker = rand_sticker()
    await message.reply_sticker(sticker="CAACAgIAAxkBAAKZy2dYnliVcgRckvQ20_89gfyEnPxkAAJEaQACOx_BSroc8BrQNBfwNgQ")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
