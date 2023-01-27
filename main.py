import telebot
import requests
import folium


bot = telebot.TeleBot('5549995858:AAFRvTwW47OIlBrsZTsbcyiinBQjpI2Zn5s')

user_id1 = ''
g = ""
ip = ""
lat = ""
prov = ''
lon = ""

@bot.message_handler(commands = ['start'])
def start(message):
    user_id1 = message.chat.id
    bot.send_message(user_id1,"Добро пожаловать в программу для определения местоположения человека по IP \nТочную геоточку программа определяет до города\nПрограмма может допустить ошибку при поиске точного местопложения в радиусе до 12 км",parse_mode='html')
    bot.send_message(user_id1,"Инструкция как узнать ip-адрес: \n https://teletype.in/@anreadyx/qTIRQpZniDH",parse_mode='html')
    main(user_id1)

@bot.message_handler()
def opis(message):
    if(g == 1):
     ip = message.text
     string1 = "." in ip
     rew = str(string1)
     if (len(ip) < 11 or len(rew) == 5):
        bot.send_message(message.chat.id,'Введите коректный IP', parse_mode='html')
     else:
        get_info_by_ip(ip, message.chat.id)
     glo1(0)
     main()
    else:
     bot.send_message(message.chat.id, "Неизесная команда, список команд - /help", parse_mode='html')

def get_info_by_ip(ip, user_id):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)
        data = {
            'IP': response.get('query'),
            'Область': response.get('isp'),
            'Провайдер': response.get('org'),
            'Страна': response.get('country'),
            'Регион': response.get('regionName'),
            'Город': response.get('city'),
            'Индекс': response.get('zip'),
            'Широта': response.get('lat'),
            'Долгота': response.get('lon'),
        }
        prov = response.get('isp')
        lat = response.get('lat')
        lon = response.get('lon')
        if prov == None:
            bot.send_message(user_id, 'Введите коректный IP', parse_mode='html')
        else:
            for k, v in data.items():
              bot.send_message(user_id, f'{k} : {v}', parse_mode='html')
            bot.send_location(user_id,latitude=lat,longitude=lon)

    except requests.exceptions.ConnectionError:
        print('Внимание! Проверьте интернет соеденение!')

def main(user_id):
    bot.send_message(user_id,"Введите ip")
    glo1(1)

def glo1(i):
    global g
    g = i
bot.polling(none_stop=True)