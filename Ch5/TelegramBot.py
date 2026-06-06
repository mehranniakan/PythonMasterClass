import telebot
from deep_translator import GoogleTranslator

API_TOKEN = '8981952554:AAFzpmAAykFPhCRgMeTYlBR98P3tbn6r3qE'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
def echo_message(message):
    try:
        translated = GoogleTranslator(source='auto', target='de').translate(message.text)
        bot.reply_to(message, translated)
    except :
        bot.reply_to(message, 'Something went wrong.')


bot.infinity_polling()