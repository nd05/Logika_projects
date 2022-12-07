from telebot import types

btn1 = types.KeyboardButton("/help")
btn2 = types.KeyboardButton("/start")
menu = types.ReplyKeyboardMarkup(resize_keyboard = True)
menu.add(btn1, btn2)

inMenu= types.InlineKeyboardMarkup(row_width= 2)
inBtn1= types.InlineKeyboardButton(text= "bt1", callback_data= "1")
inBtn2= types.InlineKeyboardButton(text= "bt2", callback_data= "2")
inBtn3= types.InlineKeyboardButton(text= "bt3", callback_data= "3")
inMenu.add(inBtn1, inBtn2, inBtn3)

inMenu1= types.InlineKeyboardMarkup(row_width= 2)
inBtn1_Menu1= types.InlineKeyboardButton(text= "a1", callback_data= "11")
inBtn2_Menu1= types.InlineKeyboardButton(text= "a2", callback_data= "12")
inBack_Menu1= types.InlineKeyboardButton(text= "Back", callback_data= "back")
inMenu1.add(inBtn1_Menu1, inBtn2_Menu1, inBack_Menu1)