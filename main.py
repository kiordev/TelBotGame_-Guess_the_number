# Guess The Number TelegramBot
# Creator: kiordev@gmail.com
# Date: 16 APRIL

import telebot
import random

# Bot Token
GuessNumberBot = telebot.TeleBot('5321322217:AAFWRjxiiOEi4QfR_WH4RsQg10mhyVngduQ')

# Start Message
@GuessNumberBot.message_handler(commands=['start'])
def start(message):
    GuessNumberBot.send_message(message.chat.id, f"Привет, <b>{message.from_user.first_name}</b> давай поиграем!", parse_mode='html')
    GuessNumberBot.send_message(message.chat.id, "Напиши /game, если готов: ")

# Main Game Code
@GuessNumberBot.message_handler(commands=['game'])
def game(message):
    ActiveGame = True

    while ActiveGame == True:
        number_to_guess = random.randrange(1, 10, 1)
        GuessNumberBot.send_message(message.chat.id, "Угадай число от 1 до 10: ")
        GuessNumberBot.send_message(message.chat.id, number_to_guess)
        ActiveGame = False


        @GuessNumberBot.message_handler()
        def get_user_variant(message):
            GuessNumberBot.send_message(message.chat.id, number_to_guess)
            message.text = int(message.text)
            if int(message.text) == number_to_guess:
                GuessNumberBot.send_message(message.chat.id, f"Молодец ты угадал, это число: {number_to_guess}")
            else:
                GuessNumberBot.send_message(message.chat.id, "Ты не угадал число!")




# Bot Is Active
GuessNumberBot.polling(none_stop=True)
