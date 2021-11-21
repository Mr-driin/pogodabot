#import OWM
#from pyowm.utils import config
#from pyowm.utils import timestamps
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import telebot

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('token')
mgr = owm.weather_manager()
bot = telebot.TeleBot("token", parse_mode=None)


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)

    w = observation.weather
    temp = w.temperature('celsius')['temp']
    answer = "В городе\поселке " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "температура сейчас в районе " + str(temp) + '\n\n'
    if temp < 10:
        answer += "заболеешь если не оденешься !!!"
    if temp > 10:
        answer += "вспотеют ноги если оденешь зимние батинки"
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True)