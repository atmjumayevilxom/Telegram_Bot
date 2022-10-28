from cgitb import html
import telebot
import pyttsx3
from telebot import types
bot = telebot.TeleBot("5347521007:AAGZWj7R3meoB7hgbIC5DKpXGQhK8BRODdw", parse_mode=None)

# @bot.message_handler(content_types=['text'])
# def send_start(message):
# 	engine = pyttsx3.init()
# 	text=message.text
# 	username=message.from_user.first_name
# 	engine.say("{},{}".format(text, username))
# 	engine.runAndWait()
# 	bot.reply_to(message, message.text+username)
# bot.infinity_polling()

@bot.message_handler(content_types=['text'])
def send_start(message):
	if message.text=="/start":
		markup = types.ReplyKeyboardMarkup()
		itembtna = types.KeyboardButton('Ovqatlar')
		itembtnv = types.KeyboardButton('Ichimliklar')
		itembtnc = types.KeyboardButton('Customer')
		itembtnd = types.KeyboardButton('Shirinliklar')
		itembtne = types.KeyboardButton('Address')
		markup.row(itembtna, itembtnv)
		markup.row(itembtnc, itembtnd, itembtne)
		bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
	elif message.text=="Ovqatlar":
		d = types.ReplyKeyboardMarkup()
		itembt1 = types.KeyboardButton('Fast Food')
		itembt2 = types.KeyboardButton('Milliy Taom')
		
		d.row(itembt1, itembt2)
		
		bot.send_message(message.chat.id, "Choose one letter:", reply_markup=d)
	elif message.text=="Fast Food":
		photo = open('1.jpg', 'rb')
		x="jkdsjkdjskfjk"
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, "<b>lavash 1ta </b> 25000ming,{}".format(x), parse_mode='HTML')
		
		
bot.infinity_polling()