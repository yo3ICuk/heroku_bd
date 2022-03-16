import sqlite3
import telebot
from datetime import datetime, timedelta
from telebot import types


bot = telebot.TeleBot("5061949277:AAFhKaHQzLrrE0SKuARQtEHjFVXmr0y7EDw")

conn = sqlite3.connect('C:\project\database.db', check_same_thread=False)
cursor = conn.cursor()
date = datetime.now()

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("сегодня")
    btn2 = types.KeyboardButton("когда")
    markup.add(btn1, btn2)    
    mesg = bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name + ". На связи Егор Новиков. Если ты тут и читаешь это сообщение, значит всё круто. Ты в том самом чат-боте проекта Торт. Продолжая, ты соглашаешься с политикой конфиденциальности http://www.consultant.ru/document/cons_doc_LAW_61801/ Что умеет этот бот? Меня зовут Торт и я могу напоминать тебе о днях рождения. Чтобы узнать у кого сегодня день рождения напиши 'сегодня'. Чтобы узнать когда день рождения у человека введите 'когда'. ", reply_markup=markup)
    


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "сегодня":
        bot.send_message(message.chat.id, 'Сегодня день рождения:')
        sql = "SELECT username FROM test WHERE birthday=?"
        for all in cursor.execute(sql, [date.strftime("%d-%m")]):
            bot.send_message(message.chat.id, all)  
    if message.text == "когда":
        ms=bot.send_message(message.chat.id, 'Введитe имя, например Новиков Егор')
        bot.register_next_step_handler(ms, name)
def name(message):
    name = message.text
    sql = "SELECT birthday FROM test WHERE username LIKE ?"
    for all in cursor.execute(sql, [name]):
        bot.send_message(message.chat.id, all)  
    
          
        
    




bot.polling(none_stop=True)