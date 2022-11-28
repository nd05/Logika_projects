from config import TOKEN
import telebot

bot =telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(massage):
    bot.send_message(massage.chat.id, 'Hi')
bot.polling(none_stop= True)