import time
from threading import Thread
from datetime import datetime
import telebot

now = str(datetime.now().day)

bot = telebot.TeleBot('5864488035:AAHqpEILOBjp2hmzJWn--UYUMuo_8Twf-b8')

userid = ['657737974','552007858','1042268328','969973418','1857763139','1455021321','1301777049','1273220489','1468584340','1664278648','1279675304','1840095109']
userName = ['Вера Казимирчук', 'Настя Штейнер','Александра Мажара','Ваня Ефимович','Мария Колосан','Варя Деева','Роман Сучков','Роман Ковальчук','Матвей Фоминцев','Маша Мутыка','Миша Белоконь','Александр Налегач',]
disableWord = ['хуй','хуйня','охуел','ахуел','пиздец','пизда','пизданул','пиздишь','пиздиш','напиздел','пиздани','ебать','наебал','ебанулся','наебнулся','ебаный','ёбаный','наебнутый','наёбнутый','пизди','ебанутый','ахуенный','ахуеный','охуенный','охуеный','блядь','блядский','блять','сука','сученок','сучка','бляха','бля','уебан','сука','чмо','ахуевший','охуевший']

def tin(user_id):
    f = open(user_id + '.txt', 'r+')
    j = str(int(f.read()) + 1)
    f.seek(0)
    f.write(j)
    f.close
def main(user_id):
    bot.send_message(user_id,"Здравствуйте, это бот для отправки номера и почты учителя автоматически после задавания вопроса по типу:\n Скиньте номер физика и тп, \nснизу пример его работы")
    photo = open('изображение_2022-12-02_133636299.png', 'rb')
    bot.send_photo(user_id, photo)

def func():
    rz = ""
    i =0
    while (i < 12):
        l = open(userid[i] + '.txt', 'r+')
        rz = rz + userName[i] + " " + l.read() + " гдз или помощи\n\n"
        l.close
        i = i + 1
    rz = rz + "\nУ всех тех, у кого 0 гдз или помощи, скиньте хоть одно до завтра иначе - временный бан на 3 дня\nУдачи)"
    bot.send_message('-1001843344430', rz)
    time.sleep(60)
def ht():
    i =0
    rz = ""
    while (i < 12):
        l = open(userid[i] + '.txt', 'r+')
        rz = rz + userName[i] + " " + l.read() + " гдз или помощи\n\n"
        l.seek(0)
        l.write('0')
        l.close
        i = i + 1
    rz = rz + "\nУ всех тех, у кого 0 гдз или помощи - временный бан на 3 дня"
    bot.send_message('-1001843344430', rz)
    time.sleep(60)

@bot.message_handler(content_types=['text'])
def opis(message):
    user_id = message.chat.id
    message_text = message.text
    message_text1 = str.lower(message.text)
    i = 0
    o = 0
    p = 0
    while (p<1366):
        t = 0
        while (i < 37):
            i = i + 1
            disable = disableWord[i]
            if disable in message_text1:
                o = 1
                t = 1
                u = len(disable)
                l = ""
                while (u != len(l)):
                    l = l + "*"
                message_text = str.lower(message_text)
                message_text = message_text.replace(disable, l)
                break
        if t == 0:
            break
        p = p + 1

    if o == 1:
       bot.delete_message(user_id, message.message_id)
       bot.send_message(user_id, "From: " + message.from_user.first_name + "\n" + message_text)
       message_text = " "


    if 'номер' in message_text or 'почту' in message_text:
        if 'биологии' in message_text or 'биологички' in message.text or 'географии' in message.text or 'географички' in message.text:
           bot.send_message(user_id,"Трегуб Оксана Володимирівна \nНомер: +380683572703\nEmail: tregub.oksanka@ukr.net")

        if 'Ольги Петровны' in message_text or 'ольги петровны' in message_text or 'ольги Петровны' in message_text or 'Ольги петровны' in message_text:
           bot.send_message(user_id,"Стеценко Ольга Петрівна \nНомер: +380965323329\nEmail: olgastop1971@gmail.com")

        if 'истории' in message_text or 'историка' in message_text:
           bot.send_message(user_id,"Родіонов Дмитро Миколайович \nНомер: +380674370525\nEmail: amiddesign2008@gmail.com")

        if 'укр лит' in message_text or 'укр. лит.' in message_text:
           bot.send_message(user_id,"Швачич Любов Сергіївна \nНомер: +380684349311\nEmail: email@gmail.com")

        if 'информатике' in message_text or 'информатички' in message_text or 'инфе' in message_text:
           bot.send_message(user_id,"Васильєва Олена Костянтинівна \nНомер: +380974235695\nEmail: email@gmail.com")

        if 'физике' in message_text or 'физика' in message_text:
           bot.send_message(user_id,"Носуль Віктор Григорович \nНомер: +380965269184\nEmail: email@gmail.com")

        if 'зар лит' in message_text or 'зарубежке' in message_text or 'зар. лит.' in message_text:
           bot.send_message(user_id,"Рудомьотова Олена Віталіївна \nНомер: +380960985788\nEmail: email@gmail.com")

        if 'химии' in message_text or 'химика' in message_text:
           bot.send_message(user_id,"Третяк Сергій Вікторович \nНомер: +380677116968\nEmail: tretyak_serge@ukr.net")

        if 'английскому' in message_text or 'англ' in message_text:
           bot.send_message(user_id,"Тітова Вікторія Анатоліївна \nНомер: +380680312010\nEmail: vk.titova.61@gmail.com")

        if 'основ' in message_text or 'основам' in message_text:
           bot.send_message(user_id,"Манагаров Олег Миколайович \nНомер: +380676275135\nEmail: olegmanagarov@gmail.com")

        if 'трудам' in message_text or 'трудов' in message_text:
           bot.send_message(user_id,"Колмакова Ольга Володимирівна \nНомер: +380986566946\nEmail: email@gmail.com")
        if 'музыке' in message_text or 'мистецтву' in message_text:
           bot.send_message(user_id,"Петрова Ірина Олександрівна \nНомер: +38011111111\nEmail: almaz512@ukr.net")

    if(message_text == '/start@nomber_emails_teachers_bot'):
        main(user_id)

    if(message_text == '/gdz_al@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_алгебра")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)
    if (message_text == '/gdz_ge@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_геометрия")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)
    if (message_text == '/gdz_xi@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_химия")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)
    if (message_text == '/gdz_fi@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_физика")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)
    if (message_text == '/gdz_bi@nomber_emails_teachers_bot'):
        tin(str(message.from_user.id))
        bot.send_message(user_id, "#гдз_биология")
        bot.delete_message(user_id, message.message_id)

    if (message_text == '/gdz_uk@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_укрлит")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)

    if (message_text == '/gdz_ge@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_география")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)

    if (message_text == '/gdz_zr@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_зарлит")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)

    if (message_text == '/gdz_fz@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_физра")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)

    if (message_text == '/gdz_mu@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_музыка")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)

    if (message_text == '/gdz_uk1@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_укрмова1")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)
    if (message_text == '/gdz_uk2@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_укрмова2")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)
    if (message_text == '/gdz_an@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_английский")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)
    if (message_text == '/gdz_inf@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_информатика")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)
    if (message_text == '/gdz_iu@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_историяукраины")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)
    if (message_text == '/gdz_vi@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_всесвітняісторія")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)
    if (message_text == '/gdz_oz@nomber_emails_teachers_bot'):
        bot.send_message(user_id, "#гдз_основыздоровья")
        tin(str(message.from_user.id))
        bot.delete_message(user_id, message.message_id)
    if ('#п' in message_text):
        tin(str(message.from_user.id))
    if ('#гдз_' in message_text):
        tin(str(message.from_user.id))
    if(message_text == '/final'):
        func()
    if(message_text == '/final1'):
        ht()


bot.polling(none_stop=True)