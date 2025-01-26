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
    # text = f'Вот и ссылочка. Ну а в ней {hlink("посылочка!", "https://i.pinimg.com/736x/ab/39/00/ab3900e9d15b6de797bef39f8da9b0bb.jpg")}' # отправляет ссылку с картинкой
    # await bot.send_message(chat_id=message.chat.id, text=text, parse_mode=ParseMode.HTML)
    await message.reply(message.text)

if __name__ == '__main__':
    dp.run_polling(bot)