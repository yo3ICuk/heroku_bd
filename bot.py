from tokenize import Name
import psycopg2
import telebot
from datetime import datetime, timedelta
from telebot import types

from config import DB_URI


bot = telebot.TeleBot("5061949277:AAFhKaHQzLrrE0SKuARQtEHjFVXmr0y7EDw")

db_connection = psycopg2.connect("postgres://ewyrrnbobbxezv:774643bf630642ef7ce029b7eb25c30fadea47f258c84067b083d4450ba71d90@ec2-54-155-5-151.eu-west-1.compute.amazonaws.com:5432/d996k5crr82vob")
db_object = db_connection.cursor()




@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("СЕГОДНЯ")
    btn2 = types.KeyboardButton("КОГДА")
    markup.add(btn1, btn2)    
    mesg1 = bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + '.\n'
    'На связи Егор Новиков')
    mesg2 = bot.send_message(message.chat.id, 'Если ты тут и читаешь это сообщение, значит всё круто.\n'
    'Ты в том самом чат-боте Проекта День Р')
    mesg3 = bot.send_message(message.chat.id, 'Чат-бот будет напоминать тебе о днях рождения твоих одноклассников и учителей.\n'
    '\n'
    'Кто сегодня празднует День Р и ждёт поздравления - жми СЕГОДНЯ\n'
    '\n'
    'Когда у твоих друзей День Р - жми КОГДА')
    mesg4 = bot.send_message(message.chat.id, "Продолжая, ты соглашаешься с политикой конфиденциальности http://www.consultant.ru/document/cons_doc_LAW_61801/", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "СЕГОДНЯ":
        bot.send_message(message.chat.id, 'Сегодня день рождения:')
        date = datetime.now()
        dates = str(date.strftime("%Y-%m-%d"))
        
        db_object.execute(f"SELECT username FROM users WHERE birthday = '{dates}'")
        all = db_object.fetchall()

        bot.send_message(message.chat.id, all)
              
    if message.text == "КОГДА":
        ms=bot.send_message(message.chat.id, 'Введитe имя, например Новиков Егор')
        bot.register_next_step_handler(ms, name)
def name(message):
    name = message.text
    db_object.execute(f"SELECT birthday FROM users WHERE username = '{name}'")
    all = db_object.fetchall()
    
    bot.send_message(message.chat.id, all)  
    
    
          
        
    




bot.polling(none_stop=True)
