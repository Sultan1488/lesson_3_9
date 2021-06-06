import telebot
from class_code_3_9_1 import KivanoBot

TOKEN = '1759358429:AAG-gT5ucOYNpClMHpF5uOLrtduE_YSNK8g'
bot = telebot.TeleBot(TOKEN)
kbot = KivanoBot()


@bot.message_handler(commands=['start', 'help'])
def show(message):
    bot.send_message(message.chat.id, kbot.help_text)


@bot.message_handler(commands=['categories'])
def categories(message):
    bot.send_message(message.chat.id, kbot.show(message))


# @bot.message_handler(commands=['product'])
# def product(message):
    # pass


if __name__ == '__main__':
    bot.polling()
