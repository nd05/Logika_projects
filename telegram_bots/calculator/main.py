# Импортируем токен из файла конфигурации
from config import TOKEN
# Импортируем файл с клавиатурами
import keyboards
# Импортируем библиотеку telebot
import telebot

# Создаем объект бот 
# Используем токен для подключения бота к телеграмму
bot = telebot.TeleBot(token = TOKEN)

#Переменная, которая будет содержать математическое выражение набраное с калькулятора

users = {}

# Декоратор, который отлавливает события сообщений со знаком /
# тоесть отлавливает команды
@bot.message_handler(commands=['start'])#в аргумент commands пишем отлавливаемую команду 
# Создаем функцию обработчик события отловленного декоратором, что описан на строку выше
def start(message):
    # Отправляем сообщение в чат
    bot.send_message(message.chat.id, # Указывакем id чата для того чтоб 
                                      # бот отправил сообщение в нужный чат
                    "Hi!", # Текст, который выведет бот в сообщение
                    reply_markup = keyboards.mainMenu # Подключаем главную клавиатуру
                    ) 


# Декоратор, который отлавливает события сообщений со знаком /
# тоесть отлавливает команды
@bot.message_handler(commands=['calculator'])# в аргумент commands пишем отлавливаемую команду 
# Создаем функцию обработчик события отловленного декоратором, что описан на строку выше
def calculator(message):
    global users
    if not message.from_user.id in users.keys():
        users[message.from_user.id]= {
            'line_of_math': "",
            'settings': {
                'delliting_Ans': True,
                'calculatin_messages': True
                },
            'conditional_flags':{
                'new': False,
                'float_number': False,
                'counter_of_*': 0,
                'counter_of_/': 0,
                'no_more_zerro': False
            }
        }
    users[message.from_user.id]['line_of_math']= ""
    # Отправляем сообщение в чат
    bot.send_message(message.chat.id, # Указывакем id чата для того чтоб 
                                      # бот отправил сообщение в нужный чат
                    "0", # Текст, который выведет бот в сообщение(0 потому как это начальное знеачение в строке калькулятора)
                    reply_markup = keyboards.calculator # Подключаем клавиатуру-калькулятор
                    )

# Декоратор, который отлавливает события сообщений со знаком /
# тоесть отлавливает команды
@bot.message_handler(commands=['settings'])# в аргумент commands пишем отлавливаемую команду
# Создаем функцию обработчик события отловленного декоратором, что описан на строку выше
def settings(message):
    global users
    if not message.from_user.id in users.keys():
        users[message.from_user.id]= {
            'line_of_math': "",
            'settings': {
                'delliting_Ans': True,
                'calculatin_messages': True
                },
            'conditional_flags':{
                'new': False,
                'float_number': False,
                'counter_of_*': 0,
                'counter_of_/': 0,
                'no_more_zerro': False
            }
        }
    bot.send_message(message.chat.id, # Указывакем id чата для того чтоб 
                                      # бот отправил сообщение в нужный чат
                    "Settings:\ndelliting_Ans: " + str(users[message.from_user.id]['settings']['delliting_Ans'])+"\ncalculatin_messages: " + str(users[message.from_user.id]['settings']['calculatin_messages']), # Текст, который выведет бот в сообщение с значением настроек
                    reply_markup = keyboards.settings # Подключаем клавиатуру-настроек
                    )

# Переключатель флага для настроек
@bot.callback_query_handler(func=lambda call:call.data in ["xor_delliting_Ans","xor_calculatin_messages"])
def callback_settings_inline(call):
    global users
    if call.data == "xor_delliting_Ans":
        users[call.from_user.id]['settings']['delliting_Ans']= users[call.from_user.id]['settings']['delliting_Ans'] ^ True
    if call.data == "xor_calculatin_messages":
        users[call.from_user.id]['settings']['calculatin_messages']= users[call.from_user.id]['settings']['calculatin_messages'] ^ True
    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Settings:\ndelliting_Ans: " + str(users[call.from_user.id]['settings']['delliting_Ans'])+"\ncalculatin_messages: " + str(users[call.from_user.id]['settings']['calculatin_messages']),reply_markup=keyboards.settings)

# Декоратор отлавливающий callback data
@bot.callback_query_handler(func=lambda call:call.data in [".","=","+","-","*","/","(",")","<=","C","0","1","2","3","4","5","6","7","8","9"])
# Создаем функцию обработчик события отловленного декоратором, что описан на строку выше
def callback_inline(call):
    global users
    if users[call.from_user.id]['conditional_flags']['new']:
        # Обнуление строки
        users[call.from_user.id]['line_of_math'] = ""
        # Обнуление флага ответственного за дробные числа
        users[call.from_user.id]['conditional_flags']['float_number']= False
        # Обнуление счётчиков ответственных за двойную постановку звёздочек и делений
        users[call.from_user.id]['conditional_flags']['counter_of_*']= 0
        users[call.from_user.id]['conditional_flags']['counter_of_/']= 0
        users[call.from_user.id]['conditional_flags']['new'] = False

    if call.data == "=":
        # Обрабатываем ошибки при запуске строки users[call.from_user.id]['line_of_math'] как пайтон кода функцией eval()
        try:
            # Проверка на специальные символоы перед "(", и если их нет добавление "*"
            for i in range(len(users[call.from_user.id]['line_of_math'])):
                if users[call.from_user.id]['line_of_math'][i] == "(" and i != 0:
                    # if users[call.from_user.id]['line_of_math'][i - 1] != "*" and users[call.from_user.id]['line_of_math'][i - 1] != "+" and users[call.from_user.id]['line_of_math'][i - 1] != "-" and users[call.from_user.id]['line_of_math'][i - 1] != "/":
                    # Добавляем знак умножить перед скобкой, если не обнаружено специального символа
                    if not users[call.from_user.id]['line_of_math'][i-1] in ["-", "+", "/", "*"]:
                        users[call.from_user.id]['line_of_math'] = users[call.from_user.id]['line_of_math'][:i] + "*" + users[call.from_user.id]['line_of_math'][i:]
            # проверка на специальные символы после ")", и если их нет добавление "*"
            for i in range(len(users[call.from_user.id]['line_of_math'])):
                if users[call.from_user.id]['line_of_math'][i] == ")" and i != len(users[call.from_user.id]['line_of_math'])-1:
                    # Добавляем знак умножить после скобки, если не обнаружено специального символа
                    if not users[call.from_user.id]['line_of_math'][i+1] in ["-", "+", "/", "*"]:
                        users[call.from_user.id]['line_of_math'] = users[call.from_user.id]['line_of_math'][:i+1] + "*" + users[call.from_user.id]['line_of_math'][i+1:]
            # Проверка на совпадение количество скобочек в выражении
            if ("(" in users[call.from_user.id]['line_of_math']) or (")" in users[call.from_user.id]['line_of_math']):
                counter_of_openers, counter_of_closers= 0, 0
                for i in users[call.from_user.id]['line_of_math']:
                    if i == "(":
                        counter_of_openers+= 1
                    if i == ")":
                        counter_of_closers+= 1
                if counter_of_openers-counter_of_closers>0:
                    for i in range(counter_of_openers-counter_of_closers):
                        users[call.from_user.id]['line_of_math']+= ")"
                if counter_of_openers-counter_of_closers<0:
                    for i in range(counter_of_closers-counter_of_openers):
                        users[call.from_user.id]['line_of_math']= "(" + users[call.from_user.id]['line_of_math']
            # Вычисление строки
            users[call.from_user.id]['line_of_math'] = str(eval(users[call.from_user.id]['line_of_math']))
            # Обнуление счётчиков ответственных за двойную постановку звёздочек и делений
            users[call.from_user.id]['conditional_flags']['counter_of_*']= 0
            users[call.from_user.id]['conditional_flags']['counter_of_/']= 0
        except:
            users[call.from_user.id]['line_of_math'] = "ERROR"
            users[call.from_user.id]['conditional_flags']['new'] = True
        # Приведение флага в состоянии True при условии удаления ответа после ввода новых чисел
        if users[call.from_user.id]['settings']['delliting_Ans']:
            users[call.from_user.id]['conditional_flags']['new'] = True
    # Удаление последнего символа в строке
    elif call.data == "<=":
        users[call.from_user.id]['line_of_math'] = users[call.from_user.id]['line_of_math'][:len(users[call.from_user.id]['line_of_math'])-1]
        if len(users[call.from_user.id]['line_of_math']) == 0:
            users[call.from_user.id]['line_of_math'] = "0"
            users[call.from_user.id]['conditional_flags']['new'] = True
    # Удалении строки
    elif call.data == "C":
        users[call.from_user.id]['line_of_math'] = "0"
        users[call.from_user.id]['conditional_flags']['new'] = True
    elif call.data:
        # Сохраняем 0 в случае, если первым симворлом пользователь ввел символ "."
        if users[call.from_user.id]['line_of_math'] == "" and call.data == ".":
            users[call.from_user.id]['line_of_math'] = "0"
        # Отключение точки при попытке повторной установки в дробное число, отключение специальных символов за исключением минуса если строка в себе не содержит чисел
        if (call.data == "." and users[call.from_user.id]['conditional_flags']['float_number']) or ((call.data in ["+", "*", "/"]) and len(users[call.from_user.id]['line_of_math'])==0):
            return
        #  Выключение нуля при условии превышения количества нулей разрешенных для ввода в условиях
        if call.data == "0" and users[call.from_user.id]['conditional_flags']['no_more_zerro']:
            return
        # Подсчет количества звёздочек и делений для органичения по количеству до двух
        if call.data == "*":
            users[call.from_user.id]['conditional_flags']['counter_of_*']+= 1
        if call.data == "/":
            users[call.from_user.id]['conditional_flags']['counter_of_/']+= 1
        if (call.data in ["*", "/"]) and (users[call.from_user.id]['conditional_flags']['counter_of_*']>=3 or users[call.from_user.id]['conditional_flags']['counter_of_/']>=3):
            return
        # Установка флага на дробность числа
        if call.data == "." and (not users[call.from_user.id]['conditional_flags']['float_number']):
            if users[call.from_user.id]['line_of_math'][-1] in ["+", "-", "*", "/"]:
                users[call.from_user.id]['line_of_math']+= "0"
            users[call.from_user.id]['conditional_flags']['float_number']= True
        # Удаление флага на дробность числа
        if call.data in ["+", "-", "*", "/", "(", ")"]:
            users[call.from_user.id]['conditional_flags']['float_number']= False
        users[call.from_user.id]['line_of_math'] = users[call.from_user.id]['line_of_math'] + call.data
    if call.message.text != users[call.from_user.id]['line_of_math'] and users[call.from_user.id]['line_of_math'] != "":   
        
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = users[call.from_user.id]['line_of_math'], reply_markup=keyboards.calculator)

#Вычисление сообщений
@bot.message_handler(content_types=['text'])
def dialog_message(message):
    global users
    if not message.from_user.id in users.keys():
        users[message.from_user.id]= {
            'line_of_math': "",
            'settings': {
                'delliting_Ans': True,
                'calculatin_messages': True
                },
            'conditional_flags':{
                'new': False,
                'float_number': False,
                'counter_of_*': 0,
                'counter_of_/': 0,
                'no_more_zerro': False
            }
        }
    users[message.from_user.id]['line_of_math']= ""
    if not users[message.from_user.id]['settings']['calculatin_messages']:
        return
    elif message.text[0] == "=":
        line_of_math= message.text[1:]
        try:
            # Проверка на специальные символоы перед "(", и если их нет добавление "*"
            for i in range(len(line_of_math)):
                if line_of_math[i] == "(" and i != 0:
                    # if line_of_math[i - 1] != "*" and line_of_math[i - 1] != "+" and line_of_math[i - 1] != "-" and line_of_math[i - 1] != "/":
                    # Добавляем знак умножить перед скобкой, если не обнаружено специального символа
                    if not line_of_math[i-1] in ["-", "+", "/", "*"]:
                        line_of_math = line_of_math[:i] + "*" + line_of_math[i:]
            # проверка на специальные символы после ")", и если их нет добавление "*"
            for i in range(len(line_of_math)):
                if line_of_math[i] == ")" and i != len(line_of_math)-1:
                    # Добавляем знак умножить после скобки, если не обнаружено специального символа
                    if not line_of_math[i+1] in ["-", "+", "/", "*"]:
                        line_of_math = line_of_math[:i+1] + "*" + line_of_math[i+1:]
            # Проверка на совпадение количество скобочек в выражении
            if ("(" in line_of_math) or (")" in line_of_math):
                counter_of_openers, counter_of_closers= 0, 0
                for i in line_of_math:
                    if i == "(":
                        counter_of_openers+= 1
                    if i == ")":
                        counter_of_closers+= 1
                if counter_of_openers-counter_of_closers>0:
                    for i in range(counter_of_openers-counter_of_closers):
                        line_of_math+= ")"
                if counter_of_openers-counter_of_closers<0:
                    for i in range(counter_of_closers-counter_of_openers):
                        line_of_math= "(" + line_of_math
            # Вычисление строки
            line_of_math = str(eval(line_of_math))
            # Обнуление счётчиков ответственных за двойную постановку звёздочек и делений
        except:
            line_of_math = "ERROR"
        bot.send_message(message.chat.id, line_of_math)

# Комада, которая запускает отлавливание сообщений в чат
bot.polling(none_stop = True)