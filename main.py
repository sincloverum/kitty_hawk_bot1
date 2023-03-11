from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5602787567:AAGYv7NrSjwyW7qPs_yvu70C060zrcfZDbQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЭто группа анонимных алкоголиков Китти Хок!\nЭто тестовый запуск нашего робота.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
