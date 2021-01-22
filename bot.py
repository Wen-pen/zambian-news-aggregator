from website import LusakaTimes, ZambianObserver, ZambianWatchdog
import telebot
import time

BOT_TOKEN = "1512838022:AAEsAeD2xbjtAg4YYozncqMek43AkHqFQZE"

bot = telebot.TeleBot(token=BOT_TOKEN)

@bot.message_handler(commands=['start'])
def reply_to_start(message):
    bot.reply_to(message, "Welcome!\n I can retrieve the news for you.\n Use /send to recieve the news")
    
@bot.message_handler(commands=["send"])
def present(message):
    
    bot.reply_to(message, "Please wait")

    lusakatimes = LusakaTimes()

    for dictionary in lusakatimes.ancList:
        bot.reply_to(message, dictionary['href'])

    zambianobserver = ZambianObserver()

    for dictionary in zambianobserver.ancList:
        bot.reply_to(message, dictionary['href'])

    zambianwatchdog = ZambianWatchdog()
    
    for dictionary in zambianwatchdog.ancList:
        bot.reply_to(message, dictionary['href'])

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)