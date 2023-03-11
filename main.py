from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5409479932:AAEPPmfzFmvLF9Y14Y8rhd578O6PX9zvek0'

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
