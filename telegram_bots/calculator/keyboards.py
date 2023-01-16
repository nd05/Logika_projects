from telebot import types

# Создаем кнопки для главной клавиатуры
mainMenuBt1 = types.KeyboardButton("/calculator")
mainMenuBt2 = types.KeyboardButton("/settings")
mainMenuBt3 = types.KeyboardButton("/start")

# Создаем главное меню
mainMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)

# Добавляем в главное меню кнопки
mainMenu.add(mainMenuBt1, mainMenuBt2, mainMenuBt3)

# Создаем инлайновую клавиатуру для калькулятора
calculator = types.InlineKeyboardMarkup()

# Добавляем рядки кнопок в клавиатуру-калькулятор
calculator.row(types.InlineKeyboardButton(text = "(", callback_data = "("),
                types.InlineKeyboardButton(text = ")", callback_data = ")"),
                types.InlineKeyboardButton(text = "<=", callback_data = "<="),
                types.InlineKeyboardButton(text = "/", callback_data = "/"))

calculator.row(types.InlineKeyboardButton(text = "7", callback_data = "7"),
                types.InlineKeyboardButton(text = "8", callback_data = "8"),
                types.InlineKeyboardButton(text = "9", callback_data = "9"),
                types.InlineKeyboardButton(text = "*", callback_data = "*"))

calculator.row(types.InlineKeyboardButton(text = "4", callback_data = "4"),
                types.InlineKeyboardButton(text = "5", callback_data = "5"),
                types.InlineKeyboardButton(text = "6", callback_data = "6"),
                types.InlineKeyboardButton(text = "-", callback_data = "-"))

calculator.row(types.InlineKeyboardButton(text = "1", callback_data = "1"),
                types.InlineKeyboardButton(text = "2", callback_data = "2"),
                types.InlineKeyboardButton(text = "3", callback_data = "3"),
                types.InlineKeyboardButton(text = "+", callback_data = "+"))

calculator.row(types.InlineKeyboardButton(text = "C", callback_data = "C"),
                types.InlineKeyboardButton(text = "0", callback_data = "0"),
                types.InlineKeyboardButton(text = ",", callback_data = "."),
                types.InlineKeyboardButton(text = "=", callback_data = "="))

settings = types.InlineKeyboardMarkup()
settings.row(
    types.InlineKeyboardButton(text = "delliting_Ans", callback_data = "xor_delliting_Ans"),
    types.InlineKeyboardButton(text = "calculatin_messages", callback_data = "xor_calculatin_messages")
)