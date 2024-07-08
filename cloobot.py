import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Приветствую")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Привет, чем помочь?")
    else:
        bot.send_message(message.from_user.id, "Привет, напиши /help")


bot.polling(non_stop=True, interval=0)
