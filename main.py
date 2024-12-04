import telebot
import json
import string
import func_TG
# def save_data(data):
#     with open("test.json" , "r" , encoding = "utf-8") as file :
#         data_from_file_str = file.read()
#     data_from_file_json:list[dict] = json.loads(data_from_file_str)
#     # data = {"name":"123"}
#     data_from_file_json.append(data)

#     with open("test.json", "w" , encoding = "utf-8") as file :
#         json_output = json.dumps(data_from_file_json , indent = 0 , ensure_ascii = False)
#         print (json_output)
#         file.write(json_output)
#     # file =  open ('file_dict_name','a+')
#     # file = open('file_dict_name','w+')
# dagits_massa = string.digits
# def check_data(massiv):
#     for i in massiv:
#         print(i)
#         if  i in  string.digits : 
#             return True
#         else :
#             return False
# сохраняем токен в переменную в виде строки
TOKEN = "7873148001:AAH1PuKXDEhrVVU8otWgFDJNERrYh2Csors"
# создаем бота и передаем токен доступа
bot = telebot.TeleBot(TOKEN)
object= ""
# reminder1 = ''
# time1 = ''
data_format="**/**/**"
col_vo = data_format.count('/')
dict_todo={}
bull = True
# resize_keyboard - разрешает автоматически изменять размер
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = telebot.types.KeyboardButton('/start')
keyboard.add(button_1)

keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)#Добавляем характеристики клавиатуре
button_link = telebot.types.InlineKeyboardButton('Тапни по мне для написания напоминания', callback_data='new_reminder')#Напишите, какое напоминание вы хотите установить
keyboard.add(button_link)


@bot.message_handler(commands=['start'])#Приветствуем
def handle_start(message):
    bot.send_message(
        message.chat.id, 
        'Привет! Это бот для создания напоминаний.', 
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: True)#создаем новое напоминание
def callback_inline(call):
    try:
        if call.message:
            if call.data == "new_reminder":
                bot.send_message(call.message.chat.id, "Я записываю...")
    except Exception as e:
        print(repr(e))
    

# @bot.message_handler(content_types=['text'])#Отправляем пользователю новое напоминание
# def handle_start_1(message):
#     reminder1=message.text
#     bot.send_message(
#         message.chat.id, 
#         'Записал.Давай назначим дату в формате **--**.'#,
#         #reply_markup=keyboard
#     )


@bot.message_handler(content_types=['text'])#Отправляем пользователю новое напоминание
def handle_object_2(message):
    global object
    object=message.text
    print(object)
    # object = object
    bot.send_message(
        message.chat.id, 
        'Записал.Давай выберем время в формате **:**:**.'#,
        #reply_markup=keyboard
    )
    bot.register_next_step_handler(message, handle_start_2) 


@bot.message_handler(content_types=['text'])#Отправляем пользователю новое напоминание
def handle_start_2(message):
    date1=message.text
    col_vo_date1=date1.count('/')
    simbol_date1 = date1.replace("/" , "")
    print(simbol_date1)
    if func_TG.check_data(simbol_date1):
        if col_vo_date1 == col_vo:
            
            bot.send_message(
                message.chat.id, 
                f'Записал. Напомню тебе об этом, когда придет время.\n С Новым Годом !'#,
                #reply_markup=keyboard
            )
            dict_todo[date1] = object
            print(dict_todo)
            func_TG.save_data(dict_todo)
    else:
        bot.send_message(
            message.chat.id, 
            'Неправильный формат даты.'#,
            #reply_markup=keyboard
        )





#import datetime
#if datetime.datetime.now() == date1 + time1 

# # добавляем декоратор, который указывает кака функция обрабатывает какой вид сообщений
# @bot.message_handler(content_types=['text'])
# # функция для обработки сообщений пользователя
# def repeat_user_message(message):
#     # в параметр message приходит объект класса telebot.types.Message
#     # он содержит в себе всю информацию о чате, пользователе и сообщении
#     bot.send_message(message.chat.id, message)


print('Сервер запущен.')
# отправка запросов обновлений
bot.polling(
    non_stop=True, # отправка запросов без остановки один за одним
    interval=1 # интервал между запросами
)