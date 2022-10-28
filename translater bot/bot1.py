
import telebot
from oxford import getDefinitions
from googletrans import Translator
translator=Translator()

bot = telebot.TeleBot("5421470438:AAG-0PTy1PFD_JSSYyT1PK3e9PhQG0I_Mss", parse_mode=None)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['text'])
def send_start(message):
    lang=translator.detect(message.text).lang
    if len(message.text.split())>2:
        dest='uz' if lang=='en' else 'en'
        bot.send_message(message.chat.id, translator.translate(message.text, dest).text)
    else:
        if lang=='en':
            word_id=message.text
        else:
            word_id=translator.translate(message.text, dest='en').text
        lookup=getDefinitions(word_id)
        if lookup:
            bot.reply_to(message, f"Word:{word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
                bot.send_voice(message.chat.id, lookup['audio'])
        else:
            bot.reply_to(message, "Bunday so'z topilmadi")
            
bot.infinity_polling()