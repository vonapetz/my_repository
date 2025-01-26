from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hlink
from aiogram.enums.parse_mode import ParseMode

BOT_TOKEN = '7805169305:AAEWQ5V6GbiWlZl6zVDepn-58UKm1uEdTHs'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Приветствую тебя!\nЯ эхо-бот. Скажи что-нибудь!;)')

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Только Бог тебе поможет...\nШучу!\nОн тоже не поможет! :*')

@dp.message()
async def send_echo(message: Message):
    text = f'Вот и ссылочка. Ну а в ней {hlink("посылачька!", "https://s00.yaplakal.com/pics/pics_original/5/5/1/17796155.jpg")}'
    await bot.send_message(chat_id=message.chat.id, text=text, parse_mode=ParseMode.HTML)
    # await message.reply(text, parse_mode=ParseMode.HTML)

if __name__ == '__main__':
    dp.run_polling(bot)