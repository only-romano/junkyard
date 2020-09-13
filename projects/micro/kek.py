import telebot
from telebot import types

token = ""
bot = telebot.TeleBot(token=token)
good_id = 1     # твой id беседы сюда чтобы его узнать напиши потом своему боту и расскоменть 12 строку
vdc_id = 2  # id чата - его тоже надо будет найти, скорее всего, закинув бот в беседу

@bot.message_handler(func=lambda m: True)
def any_msg(message):
    chat_id = message.chat.id
    #print(chat_id)
    if (chat_id == good_id):
        message_id = message.message_id
        bot.forward_message(vdc_id, chat_id, message_id)

if __name__ == "__main__":
    bot.polling(none_stop=True)
