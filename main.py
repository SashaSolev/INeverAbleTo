from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
from background import keep_alive


dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
  await message.answer('/send и далее сообщение \nПример: /send выспаться')
@dp.message()
async def send(message: Message):
  string = message.text
  if string:
    string_list = string.split(' ')
    if string_list[0] == '/send':
      if message.text:
        string = message.text.replace('/send', ' ').lower()
      chat_id1 = '-1002006315849'
      await message.answer("Отправлено")
      await Bot(token='6959940229:AAEmMGFbrSGwNvvfeYLhhtDgDWENJk5IlMU').send_message(chat_id=chat_id1, text=string)

async def main():
  bot = Bot(token='6959940229:AAEmMGFbrSGwNvvfeYLhhtDgDWENJk5IlMU')
  keep_alive()
  await dp.start_polling(bot)

if __name__ == "__main__":
  print('start')
  asyncio.run(main())