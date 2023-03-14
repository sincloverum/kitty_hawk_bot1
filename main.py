from aiogram import Bot, Dispatcher, executor, types
from config import Token

bot = Bot(Token)
dp = Dispatcher(bot)

@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    user_name = message.new_chat_members[0].first_name
    bot.send_message(message.chat.id, "Добро пожаловать, {0}!".format(user_name))

if __name__ == "__main__":
    executor.start_polling(dp)




