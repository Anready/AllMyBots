import time
import telebot
import requests
from geopy.geocoders import Nominatim
from telebot import types

from itertools import groupby

bot = telebot.TeleBot('5568749424:AAGVEEjzwKmYtzbFM1XZKorm563mERLA88I')


user_id1 = ''
g = ""
ip = ""
lat = ""
prov = ''
q = 0
lon = ""
a = ""
s = 0.1
d = 0.1
f = 0.1
g = 0.1
h = 0.1
j = 0.1
k = ""
all = []


def main(user_id):
    my_user_id = user_id
    all.append(my_user_id)

    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_geo1 = types.KeyboardButton(text="Погода в Киеве")
    button_geo3 = types.KeyboardButton(text="Погода в Кривом Роге")
    button_geo = types.KeyboardButton(text="Погода по местоположению", request_location=True)
    button_geo4 = types.KeyboardButton(text="Погода в Днепре")
    button_geo5 = types.KeyboardButton(text="Погода в Одессе")
    keyboard.add(button_geo1,button_geo3)
    keyboard.add(button_geo)
    keyboard.add(button_geo4,button_geo5)
    bot.send_message(user_id,"Введите 🗺город🗺 чтобы белка определила погоду. \nИли вы можете найти погоду по 🧭местоположению🧭", reply_markup=keyboard)

@bot.message_handler(content_types=['location'])
def location (message):
    if message.location is not None:
        geolocator = Nominatim(user_agent="here")
        a = [message.location.latitude, message.location.longitude]
        geos = geolocator.reverse(a, language='ru')  # определяем адрес по координатам
        geoloc = geos.address
        lst = geoloc.split(',')
        country = lst[0]
        city_name = country
        first_string = lst[4]
        first_string = first_string[1:]
        get_info_by_ip(first_string, message.chat.id)


@bot.message_handler(commands = ['start'])
def start(message):
    user_id = message.chat.id
    main(user_id)

@bot.message_handler(commands = ['restart'])
def start(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Бот успешно обновлен")
    main(user_id)

@bot.message_handler(commands=['?K5&7z{wk&YT7fR41WES,z$zfeNEgPct6LUFuhc$'])
def callback_worker(message):
    new_x = [el for el, _ in groupby(all)]
    for i in range(len(new_x)):
        bot.send_message(new_x[i], "Внимание бот был обновлен! Напишите /restart для обновления")

def get_info_by_ip(city, user_id):
    try:
        res = requests.get(url=f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=24a9a30b015719f513b372d4fd5e0afd&units=metric&lang=ru')
        data = res.json()
        a =str.title(data['list'][0]['weather'][0]['description'])
        s =data['list'][0]['main']['temp']
        d =data['list'][0]['main']['feels_like']
        f =data['list'][0]['main']['temp_min']
        g =data['list'][0]['main']['temp_max']
        h =data['list'][0]['visibility']
        j =data['list'][0]['wind']['speed']
        bot.send_message(user_id, f"🗺Белка прыгает в город {city}🗺")
        bot.send_sticker(user_id, 'CAACAgIAAxkBAAIBG2LtBUne_z8IqZKNGCa4OvKQlFNeAAKaAAP3AsgP0dUG8v161DgpBA')
        time.sleep(5)
        bot.send_message(user_id, f"🐿Погода найдена!🐿")
        time.sleep(2)
        bot.send_message(user_id, f"🕛 Сейчас 🕛: {a}\n🌡 Температура 🌡: {s}\n🔥❄ Ощущается как ❄🔥: {d}\n❄🌡 Минимальная температура сегодня 🌡❄: {f}\n🌡🔥 Максимальная температура сегодня 🔥🌡: {g}\n👁Видимость👁: {h} метров\nСкорость ветра🌬: {j}м/с")
    except Exception as e:
        bot.send_message(user_id, "‼🗺Белка не нашла этот город на карте: введите его корретно🗺‼", parse_mode='html')
        pass



@bot.message_handler(content_types=['text'])
def opis(message):
    if(message.text == 'Погода в Киеве'):
        get_info_by_ip("Киев", message.chat.id)
    elif(message.text == 'Погода в Кривом Роге'):
        get_info_by_ip("Кривой рог", message.chat.id)
    elif(message.text == 'Погода в Днепре'):
        get_info_by_ip("Днепр", message.chat.id)
    elif(message.text == 'Погода в Одессе'):
        get_info_by_ip("Одесса", message.chat.id)
    elif (message.text == 'Москва'):
        bot.send_message(message.chat.id, "‼🗺А разве этот этот город развве еще есть?🗺‼", parse_mode='html')
        bot.send_message(message.chat.id, "-Алё привет Мышка\n-Привет что надо?\n-А Моква еще есть?\n-Да, а что?\n-Да не ничего... Спасибо пока!\n-Пока", parse_mode='html')
        time.sleep(2)
        bot.send_message(message.chat.id, "Ладно...", parse_mode='html')
        get_info_by_ip("Москва", message.chat.id)
    elif (message.text == 'Moscow'):
        bot.send_message(message.chat.id,"‼🗺А разве этот этот город развве еще есть?🗺‼", parse_mode='html')
        bot.send_message(message.chat.id,"-Алё привет Мышка\n-Привет что надо?\n-А Моква еще есть?\n-Да, а что?\n-Да не ничего... Спасибо пока!\n-Пока",parse_mode='html')
        time.sleep(2)
        bot.send_message(message.chat.id, "Ладно...", parse_mode='html')
        get_info_by_ip("Москва", message.chat.id)
    else:
        get_info_by_ip(message.text, message.chat.id)



bot.polling(none_stop=True)
