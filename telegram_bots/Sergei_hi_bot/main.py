from config import TOKEN
import keyboards
import json, os, telebot

bot =telebot.TeleBot(TOKEN)
users_data= {}
with open(os.path.dirname(os.path.abspath(__file__))+'/users_id.json', "r") as file:
    users_data= json.load(file)

@bot.message_handler(commands=['start'])
def start(massage):
    print(massage.from_user.id)
    if int(massage.from_user.id) not in users_data:
        print(users_data)
        bot.send_message(massage.chat.id, 'Hi', reply_markup = keyboards.menu)
        users_data[massage.from_user.id]= {'username':massage.from_user.username, 'first_name':massage.from_user.first_name, 'last_name':massage.from_user.last_name}
    else:
        bot.send_message(massage.chat.id, 'Hi, I know you.\nYour name is '+users_data[massage.from_user.id]['first_name'],reply_markup = keyboards.menu)
    with open(os.path.dirname(os.path.abspath(__file__))+'/users_id.json', "w") as file:
        print(users_data)
        json.dump(users_data, file, indent= 2)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "help", reply_markup = keyboards.inMenu)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "1":
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = "help^2", reply_markup=keyboards.inMenu1)
    if call.data == "back":
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = "help", reply_markup=keyboards.inMenu)

bot.polling(none_stop= True)