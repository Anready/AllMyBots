from datetime import datetime
import telebot
import cv2
import random
from telebot import types

message = ""
global water
water = {}
photo = 0
u = 0
now = str(datetime.now().day)
bot = telebot.TeleBot('5788120027:AAHWHyLVtdOZDyHCEt3AygN-8OwocIx0IPg')

def biggest():
    i = 1
    max = {"min":50}
    while (i<8):
        hash1 = CalcImageHash(f"{i}.jpg")
        hash2 = CalcImageHash("downloaded_image.jpg")
        if(max.get("min") > CompareHash(hash1, hash2)):
            max.update({"min":CompareHash(hash1, hash2)})
        i += 1
    print (max.get("min"))
    return max.get("min")

def tin(kill = ""):
    if kill == "t":
        f = open('a.txt', 'r+')
        j = f.read()
        f.seek(0)
        f.close
        return int(j)
    elif kill == "kill":
        f = open('a.txt', 'r+')
        f.seek(0)
        f.write("3")
        f.close
    else:
        f = open('a.txt', 'r+')
        j = str(int(f.read()) - 1)
        f.seek(0)
        f.write(j)
        f.close


def CalcImageHash(FileName):
    image = cv2.imread(FileName)
    resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    avg = gray_image.mean()
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)


    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash = _hash + "1"
            else:
                _hash = _hash + "0"

    return _hash

def CompareHash(hash1, hash2):
    l = len(hash1)
    i = 0
    count = 0
    while i < l:
        if hash1[i] != hash2[i]:
            count = count + 1
        i = i + 1
    return count


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Need water")
    btn2 = types.KeyboardButton("No more need for water")
    markup.add(btn1, btn2)
    if message.chat.id == 1841947823:
        bot.send_message(message.chat.id, "Привет", reply_markup=markup)
    elif message.chat.id == 1840095109 or message.chat.id ==5599897484:
        bot.send_message(message.chat.id, "Привет")
    else:
        markup1 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Tixan", url='http://tixan.unaux.com/')
        markup1.add(button1)
        bot.send_message(message.chat.id, "Привет, к сожелению это не публичный бот, если хочешь то посети наш сайт", reply_markup=markup1)

@bot.message_handler(commands=['water'])
def main(message):
    if message.chat.id == 1841947823 and u != 1:
        glo1(1)
        if random.randint(1, 2) == 1:
            water.update({'water':1840095109})
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="Задание выполнил", callback_data="button1"))
            bot.send_message(1840095109, "Сегодня ваша очередь ходьбы за водой", reply_markup=keyboard)
        else:
            water.update({'water': 5599897484})
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="Задание выполнил", callback_data="button1"))
            bot.send_message(5599897484, "Сегодня ваша очередь ходьбы за водой", reply_markup=keyboard)

        bot.send_message(message.chat.id, "Сообщение об отправке за водой отправлено")

@bot.message_handler(commands=['nowater'])
def main(message):
    if message.chat.id == 1841947823 and u == 1:
        glo(0)
        glo1(0)
        tin("kill")
        bot.send_message(message.chat.id, "Сообщение о неприносе воды отправлено")
        bot.send_message(water.get('water'), "Вы не доставили воду вовремя!")
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Да", callback_data="button2"))
        keyboard.add(types.InlineKeyboardButton(text="Нет", callback_data="button3"))
        bot.send_message(message.chat.id, "Сделать перенаправку задания?", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    user_id = call.from_user.id
    if call.data == "button1" and u == 1:
        glo(1)
        bot.send_message(user_id, "Отправьте фото с наполненой банкой")

    if call.data == "button2":
        bot.send_message(1841947823, "Хорошо, сделаю перенаправку")
        bot.send_message(water.get('water'), "Вы не доставили воду вовремя!")
        glo1(1)
        if water.get('water') == 1840095109:
            water.update({'water': 5599897484})
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="Задание выполнил", callback_data="button1"))
            bot.send_message(5599897484, "Пойдите за водой", reply_markup=keyboard)
        else:
            water.update({'water': 1840095109})
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="Задание выполнил", callback_data="button1"))
            bot.send_message(1840095109, "Пойдите за водой", reply_markup=keyboard)

    if call.data == "button3":
        bot.send_message(1841947823, "Хорошо!")

@bot.message_handler(content_types=['photo'])
def opis(message):
    user_id = message.chat.id
    if photo != 0:
        try:
            file_id = message.photo[-1].file_id
            file_info = bot.get_file(file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            with open("downloaded_image.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            if biggest() < 13 and biggest() != 1 or biggest() != 0 and tin("t") >= 0:
                glo1(0)
                bot.send_message(user_id, "Спасибо, задача выполнена успешно!")
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(types.InlineKeyboardButton(text="Нет", callback_data="button2"))
                keyboard.add(types.InlineKeyboardButton(text="Да", callback_data="button3"))
                photo_id = message.photo[-1].file_id
                bot.send_photo(1841947823, photo_id)
                bot.send_message(1841947823, "Задача выполнена успешно! \n\nВода набрана?",reply_markup=keyboard)
                tin("kill")
                glo(0)
            elif biggest() == 1 or biggest() == 0 and tin("t") >= 1:
                bot.send_message(user_id, f"Вы отправили исходное фото! (Осталось {tin('t')} попытки)")
                tin("")
            elif tin("t") >= 1:
                bot.send_message(user_id, f"Я не распознал фото, сфоткайте под другим углом или набирите воду (Осталось {tin('t')} попытки)")
                tin("")
            else:
                glo1(0)
                bot.send_message(user_id, "Попытки истрачены, сообщаю администратору о не выполнении задачи...")
                glo(0)
                tin("kill")
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(types.InlineKeyboardButton(text="Нет", callback_data="button2"))
                keyboard.add(types.InlineKeyboardButton(text="Да", callback_data="button3"))
                photo_id = message.photo[-1].file_id
                bot.send_photo(1841947823, photo_id)
                bot.send_message(1841947823, "Мне не удалось определить набрана ли вода, она набрана?", reply_markup=keyboard)
        except Exception as e:
            bot.reply_to(message, e)

def glo(i):
    global photo
    photo = i

def glo1(i):
    global u
    u = i

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Need water"):
       if message.chat.id == 1841947823 and u != 1:
        glo1(1)
        if random.randint(1, 2) == 1:
            water.update({'water':1840095109})
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="Задание выполнил", callback_data="button1"))
            bot.send_message(1840095109, "Сегодня ваша очередь ходьбы за водой", reply_markup=keyboard)
        else:
            water.update({'water': 5599897484})
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="Задание выполнил", callback_data="button1"))
            bot.send_message(5599897484, "Сегодня ваша очередь ходьбы за водой", reply_markup=keyboard)

        bot.send_message(message.chat.id, "Сообщение об отправке за водой отправлено")

    if(message.text == "No more need for water"):
        if message.chat.id == 1841947823 and u == 1:
            glo(0)
            glo1(0)
            tin("kill")
            bot.send_message(message.chat.id, "Сообщение о неприносе воды отправлено")
            bot.send_message(water.get('water'), "Вы не доставили воду вовремя!")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="Да", callback_data="button2"))
            keyboard.add(types.InlineKeyboardButton(text="Нет", callback_data="button3"))
            bot.send_message(message.chat.id, "Сделать перенаправку задания?", reply_markup=keyboard)


bot.polling(none_stop=True)
