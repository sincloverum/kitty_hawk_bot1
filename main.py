"""
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''

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
"""

from telebot import TeleBot
from pyTelegramBotCAPTCHA import CaptchaManager

bot = TeleBot('')
captcha_manager = CaptchaManager(bot.get_me().id)


# Message handler for new chat members
@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
    for new_user in message.new_chat_members:
        captcha_manager.restrict_chat_member(bot, message.chat.id, new_user.id)
        captcha_manager.send_new_captcha(bot, message.chat, new_user)


# Callback query handler
@bot.callback_query_handler(func=lambda callback: True)
def on_callback(callback):
    captcha_manager.update_captcha(bot, callback)


# Handler for correct solved CAPTCHAs
@captcha_manager.on_captcha_correct
def on_correct(captcha):
    bot.send_message(captcha.chat.id, "Congrats! You solved the CAPTCHA!")
    captcha_manager.unrestrict_chat_member(bot, captcha.chat.id, captcha.user.id)
    captcha_manager.delete_captcha(bot, captcha)


# Handler for wrong solved CAPTCHAs
@captcha_manager.on_captcha_not_correct
def on_not_correct(captcha):
    if (captcha.incorrect_digits == 1 and captcha.previous_tries < 2):
        captcha_manager.refresh_captcha(bot, captcha)
    else:
        bot.kick_chat_member(captcha.chat.id, captcha.user.id)
        bot.send_message(captcha.chat.id, f"{captcha.user.first_name} failed solving the CAPTCHA and was banned!")
        captcha_manager.delete_captcha(bot, captcha)


# Handler for timed out CAPTCHAS
@captcha_manager.on_captcha_timeout
def on_timeout(captcha):
    bot.kick_chat_member(captcha.chat.id, captcha.user.id)
    bot.send_message(captcha.chat.id, f"{captcha.user.first_name} did not solve the CAPTCHA and was banned!")
    captcha_manager.delete_captcha(bot, captcha)


bot.polling()
