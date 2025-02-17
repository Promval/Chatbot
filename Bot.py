import telebot

bot = telebot.TeleBot('7321533603:AAGQGhWtG3MzrEQSz6AuIRkSnX0_4V7a9B4')

@bot.message_handler(commands=['start', 'main',])
def main(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Привет')

bot.polling(none_stop=True)

