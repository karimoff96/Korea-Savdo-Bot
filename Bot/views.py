import types
from telebot import *
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from telebot.types import InputMediaPhoto
from .controller import *

# Create your views here.


bot = TeleBot('5176543389:AAHidLypZBK6qzGlnlWJdT71eShOcwEANxE', parse_mode="HTML")

hideBoard = types.ReplyKeyboardRemove()
Admin = 419717087


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse("<a href='http://t.me/dkarimoff96'>Created by</>")
    if request.method == 'POST':
        bot.process_new_updates([
            telebot.types.Update.de_json(
                request.body.decode("utf-8")
            )
        ])
        return HttpResponse(status=200)


@bot.message_handler(commands=["start"])
def start(message):
    if User.objects.filter(user_id=message.from_user.id).exists():
        print(1)
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('🔰Yordam')
        btn1 = types.KeyboardButton('🚘Avtomobil')
        btn2 = types.KeyboardButton('📄E`lonlarim')
        # btn2 = types.KeyboardButton('Telefon')
        # btn3 = types.KeyboardButton('Notebook')
        markup.add(btn1, btn, btn2)
        bot.send_message(message.chat.id, "<b>📜E`lon turini tanlang!</b>", reply_markup=markup)
        bot_user = User.objects.get(user_id=message.from_user.id)
        elon = Elon.objects.create(
            user=bot_user
        )
        elon.save()

    else:
        print('else')
        text = f'<i>Assalomu alaykum {message.from_user.first_name}.\n<b>📜E`lon turini tanlang!</b></i>'
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('🔰Yordam')
        btn1 = types.KeyboardButton('🚘Avtomobil')
        btn2 = types.KeyboardButton('📄E`lonlarim')
        # btn2 = types.KeyboardButton('Telefon')
        # btn3 = types.KeyboardButton('Notebook')
        markup.add(btn1, btn, btn2)
        bot.send_message(message.chat.id, text, reply_markup=markup)
        bot_user = User.objects.create(user_id=message.from_user.id, username=message.from_user.username)
        bot_user.save()
        elon = Elon.objects.create(
            user=bot_user
        )
        elon.save()


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot_user = User.objects.get(user_id=message.from_user.id)
    bot_elon = Elon.objects.get(user=bot_user, active=False)
    print(message.text)
    if message.text == '🚘Avtomobil':
        bot_elon.category = message.text[1:]
        bot_elon.step = 1
        bot_elon.save()
        text = f'<b><i>📋{bot_elon.category}</i> rukunida e`lon berish.\nSizga bir necha savollar beriladi.\nBarchasiga to`liq va aniq javob bering.\nYakunida barcha ma`lumotlaringiz to`gri bo`lsa "OK" tugmasini bosing va arizangiz Adminga yuboriladi.</b> '
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn1 = types.KeyboardButton('🛑Bekor qilish')
        markup.add(btn1)
        bot.send_message(message.chat.id, text, reply_markup=markup)
        bot.send_message(message.chat.id, "<b>👤Ismingizni kiriting</b>")
    elif bot_elon.step == 1 and len(
            message.text) > 0 and message.text != '🛑Bekor qilish' and message.text != '🔰Yordam' and message.text != '📄E`lonlarim':
        print('ism')
        bot_elon.first_name = message.text
        bot_elon.step = 2
        bot_elon.save()
        bot.send_message(message.chat.id, '<b>📞Telefon raqamingizni kiriting: \nMasalan:</b> <i>01012344321</i>')
    elif bot_elon.step == 2 and len(message.text) == 11:
        if message.text.isdigit():
            bot_elon.phone_number = message.text
            bot_elon.step = 3
            bot_elon.save()
            bot.send_message(message.chat.id, "<b>🏠Manzilni kiriting:\nMasalan:</b><i>Busan, Gimhae</i>")
        else:
            bot.send_message(message.chat.id, "<code>Iltimos namunada keltirilgan shakldagi raqam kiriting</code>")
    elif bot_elon.step == 3 and len(
            message.text) > 0 and message.text != '🛑Bekor qilish' and message.text != '🔰Yordam' and message.text != '📄E`lonlarim':
        bot_elon.address = message.text
        bot_elon.step = 4
        bot_elon.save()
        bot.send_message(message.chat.id, "<b>🚘Avtomobil nomi:\nMasalan:</b><i>Hyundai Sonata N20</i>")
    elif bot_elon.step == 4 and len(
            message.text) > 0 and message.text != '🛑Bekor qilish' and message.text != '🔰Yordam' and message.text != '📄E`lonlarim':
        bot_elon.model = message.text
        bot_elon.step = 5
        bot_elon.save()
        bot.send_message(message.chat.id, "<b>⚙Ishlab chiqarilgan yili:\nMasalan:</b><i>2005</i>")
    elif bot_elon.step == 5 and len(
            message.text) == 4 and message.text != '🛑Bekor qilish' and message.text != '🔰Yordam' and message.text != '📄E`lonlarim':
        print(message.text)
        print(type(message.text))
        if 1999 <= int(message.text) <= 2022:
            print('kirdiiii')
            bot_elon.year = message.text
            bot_elon.step = 6
            bot_elon.save()
            bot.send_message(message.chat.id,
                             "<b>🐎Probeg: Avtomobilning bosib o`tgan asosiy kilometrajini kiriting</b> <i><b>Masalan:</b>142*** yoki 142320 </i>")
        else:
            bot.send_message(message.chat.id,
                             "<code>‼️Iltimos 2000-dan hozirga qada bo`lgan yillarni kiriting!</code>")
    elif bot_elon.step == 6 and 0 < len(message.text) < 7 and message.text[0:2].isdigit():
        bot_elon.journey = message.text
        bot_elon.step = 7
        bot_elon.save()
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('🟢Legal')
        btn1 = types.KeyboardButton('🔴Nelegal')
        markup.add(btn, btn1)
        bot.send_message(message.chat.id, '<b>📁Yuridik holati:</b>', reply_markup=markup)
    elif bot_elon.step == 7 and message.text == '🟢Legal':
        bot_elon.step = 8
        bot_elon.policy = message.text[1:]
        bot_elon.save()
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('✳️Avtomat')
        btn1 = types.KeyboardButton('❇️Mexanika')
        btn2 = types.KeyboardButton('❎Boshqa')
        markup.add(btn, btn1, btn2)
        bot.send_message(message.chat.id, '<b>⏫Korobka</b>', reply_markup=markup)
    elif bot_elon.step == 7 and message.text == '🔴Nelegal':
        bot_elon.step = 8
        bot_elon.policy = message.text[1:]
        bot_elon.save()
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('✳️Avtomat')
        btn1 = types.KeyboardButton('❇️Mexanika')
        btn2 = types.KeyboardButton('❎Boshqa')
        markup.add(btn, btn1, btn2)
        bot.send_message(message.chat.id, '<b>⏫Korobka</b>', reply_markup=markup)
    elif bot_elon.step == 8 and message.text == '✳️Avtomat':
        bot_elon.step = 9
        bot_elon.korobka = message.text[1:]
        bot_elon.save()
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('🟠Benzin')
        btn1 = types.KeyboardButton('🔵LPG')
        btn2 = types.KeyboardButton('⚫️Boshqa')
        markup.add(btn, btn1, btn2)
        bot.send_message(message.chat.id, '<b>⛽Yoqilg`i turi</b>', reply_markup=markup)
    elif bot_elon.step == 8 and message.text == '❇️Mexanika':
        bot_elon.step = 9
        bot_elon.korobka = message.text[1:]
        bot_elon.save()
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('🟠Benzin')
        btn1 = types.KeyboardButton('🔵LPG')
        btn2 = types.KeyboardButton('⚫️Boshqa')
        markup.add(btn, btn1, btn2)
        bot.send_message(message.chat.id, '<b>⛽Yoqilg`i turi</b>', reply_markup=markup)
    elif bot_elon.step == 8 and message.text == '❎Boshqa':
        bot_elon.step = 9
        bot_elon.korobka = message.text[1:]
        bot_elon.save()
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('🟠Benzin')
        btn1 = types.KeyboardButton('🔵LPG')
        btn2 = types.KeyboardButton('⚫️Boshqa')
        markup.add(btn, btn1, btn2)
        bot.send_message(message.chat.id, '<b>⛽Yoqilg`i turi</b>', reply_markup=markup)
    elif bot_elon.step == 9 and message.text == '🟠Benzin' and message.text != '🛑Bekor qilish' and message.text != '🔰Yordam' and message.text != '📄E`lonlarim':
        bot_elon.step = 10
        bot_elon.fuel = message.text[1:]
        bot_elon.save()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        text2 = "<b>ℹQo`shimcha ma`limot:\nMasalan:</b> <i>Kamchiligi, qulayliklari, aybi va ustunliklari</i>"
        btn1 = types.KeyboardButton('🛑Bekor qilish')
        markup.add(btn1)
        bot.send_message(message.chat.id, text2, reply_markup=markup)
    elif bot_elon.step == 9 and message.text == '🔵LPG' and message.text != '🛑Bekor qilish' and message.text != '🔰Yordam' and message.text != '📄E`lonlarim':
        bot_elon.step = 10
        bot_elon.fuel = message.text[1:]
        bot_elon.save()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        text2 = "<b>ℹQo`shimcha ma`limot:\nMasalan:</b> <i>Kamchiligi, qulayliklari, aybi va ustunliklari</i>"
        btn1 = types.KeyboardButton('🛑Bekor qilish')
        markup.add(btn1)
        bot.send_message(message.chat.id, text2, reply_markup=markup)
    elif bot_elon.step == 9 and message.text == '⚫️Boshqa' and message.text != '🛑Bekor qilish' and message.text != '🔰Yordam' and message.text != '📄E`lonlarim':
        bot_elon.step = 10
        bot_elon.fuel = message.text[1:]
        bot_elon.save()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        text2 = "<b>ℹQo`shimcha ma`limot:\nMasalan:</b> <i>Kamchiligi, qulayliklari, aybi va ustunliklari</i>"
        btn1 = types.KeyboardButton('🛑Bekor qilish')
        markup.add(btn1)
        bot.send_message(message.chat.id, text2, reply_markup=markup)
    elif bot_elon.step == 10 and len(
            message.text) > 0 and message.text != '🛑Bekor qilish' and message.text != '🔰Yordam' and message.text != '📄E`lonlarim':
        bot_elon.step = 11
        bot_elon.comment = message.text[1:]
        bot_elon.save()
        bot.send_message(message.chat.id, "<b>💸Narxini kiriting:\nMasalan:</b> <i>1600000</i>")
    elif bot_elon.step == 12 and message.text != '🛑Bekor qilish':
        bot.send_message(message.chat.id, "<b>🌅Iltimos rasm yuboring!</b>")
    elif message.text == "🔰Yordam":
        bot.send_message(message.chat.id,
                         '<u>ℹ️Bu bot orqali telegram kanalda o`zingizning elonlaringizni qoldirishingiz mumkin.\nEloningiz bo`yicha anketani to`ldiring. \n<i>Bizning kanalga a`zo bo`ling: https://t.me/korea_elonlar\nE`lon berish uchun: https://t.me/korea_savdo_bot</i></u>')
    elif message.text == '🛑Bekor qilish':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('🔰Yordam')
        btn1 = types.KeyboardButton('🚘Avtomobil')
        btn2 = types.KeyboardButton('📄E`lonlarim')
        # btn2 = types.KeyboardButton('Telefon')
        # btn3 = types.KeyboardButton('Notebook')
        markup.add(btn1, btn, btn2)
        bot.send_message(message.chat.id, "<b>📜E`lon turini tanlang!</b>", reply_markup=markup)
        bot_elon.step = 0
        bot_elon.save()

    elif bot_elon.step == 11 and message.text.isdigit():
        bot_elon.step = 12
        bot_elon.price = message.text
        bot_elon.save()
        bot.send_message(message.chat.id,
                         "<i><b>‼️Avtomobilning 3 dona sur`atini, 1 tadan qilib aloxida qadamlarda yuboring\nE`tibor qiling, rasmlar 'FILE' formatida bo`lmasin!!</b></i>")
        bot.send_message(message.chat.id, "<b>1️⃣Datlabki ramsni yuboring</b>")

        # Admin Mode
    elif message.text == '/send':
        if message.chat.id == Admin:
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            b = types.KeyboardButton('🔙Ortga')
            markup.add(b)
            mesg = bot.send_message(message.chat.id, '<code>‼️E`lonni kiriting:</code>', reply_markup=markup)
            bot.register_next_step_handler(mesg, test)
    elif message.text == "/stats":
        print('stats')
        if message.chat.id == Admin:
            print(Elon.objects.filter(active=True).count())
            user = len(User.objects.all())
            elon = len(Elon.objects.filter(active=True))
            bot.send_message(message.chat.id,
                             f'🔰<b><i>Bot statistics:</i></b>\n<b>📄Elonlar soni:</b> {elon}\n👥<b>Foydalanuvchilar:</b> {user}\n🧑🏻‍💻<b>Creator:</b><i> @dkarimoff96</i>')
    elif message.text == "📄E`lonlarim":
        elon = Elon.objects.filter(user__user_id=message.from_user.id, active=True)
        if len(elon) > 0:
            for bot_elon in elon:
                text = f"<u><b>📋E`loningiz ma`lumotlari:</b></u>\n<b>👉Elon turi:</b> <i>{bot_elon.category}</i>.\n👤<b>Ism:</b> <i>{bot_elon.first_name}.</i>\n📞<b>Tel raqam:</b> <i>{bot_elon.phone_number}.</i>\n<b>🏠Manzil:</b> <i>{bot_elon.address}</i>.\n 🚘<b>Nomi:</b> <i>{bot_elon.model}</i>.\n⚙️<b>Yili:</b> <i>{bot_elon.year}</i>.\n🐎<b>Probegi:</b> <i>{bot_elon.journey} km</i>.\n📁<b>Yuridik holati:</b> <i>{bot_elon.policy}.</i> \n⏫<b>Korobka:</b> <i>{bot_elon.korobka}</i>.\n⛽️<b>Yonilg`i:</b> <i>{bot_elon.fuel}</i>.\nℹ️<b>Qo`shimcha:</b> <i>{bot_elon.comment}</i>\n💸<b>Narxi:</b> <i>{bot_elon.price} ￦</i> \n\n<i>Bizning kanalga a`zo bo`ling: https://t.me/korea_elonlar\nE`lon berish uchun: https://t.me/korea_savdo_bot</i>"
                bot.send_media_group(chat_id=message.from_user.id,
                                     media=[InputMediaPhoto(bot_elon.image, caption=text, parse_mode="HTML"),
                                            InputMediaPhoto(bot_elon.image1),
                                            InputMediaPhoto(bot_elon.image2)])
        else:
            print('elon yoq')
            bot.send_message(message.from_user.id, "<pre>‼️E`lon mavjud emas!</pre>")
    elif message.text == '🔙Ortga':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('🔰Yordam')
        btn1 = types.KeyboardButton('🚘Avtomobil')
        btn2 = types.KeyboardButton('📄E`lonlarim')
        # btn2 = types.KeyboardButton('Telefon')
        # btn3 = types.KeyboardButton('Notebook')
        markup.add(btn1, btn, btn2)
        bot.send_message(message.chat.id, "<b>📜E`lon turini tanlang</b>", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "<pre>‼️Iltimos to`g`ri ma`lumot kiriting!</pre>")


def test(message):
    if message.text == '🔙Ortga':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        btn = types.KeyboardButton('🔰Yordam')
        btn1 = types.KeyboardButton('🚘Avtomobil')
        btn2 = types.KeyboardButton('📄E`lonlarim')
        # btn2 = types.KeyboardButton('Telefon')
        # btn3 = types.KeyboardButton('Notebook')
        markup.add(btn1, btn, btn2)
        bot.send_message(message.chat.id, "<b>📜E`lon turini tanlang</b>", reply_markup=markup)

    else:
        for m in User.objects.all():
            bot.copy_message(chat_id=m.user_id, from_chat_id=message.chat.id, message_id=message.id)
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('🔰Yordam')
        btn1 = types.KeyboardButton('🚘Avtomobil')
        btn2 = types.KeyboardButton('📄E`lonlarim')
        # btn2 = types.KeyboardButton('Telefon')
        # btn3 = types.KeyboardButton('Notebook')
        markup.add(btn1, btn, btn2)
        bot.send_message(message.from_user.id, '<code><i>E`lon foydalanuvchilarga muvaffaqiyatli jo`natildi</i></code>',
                         reply_markup=markup)


@bot.message_handler(content_types=['photo', 'file'])
def photo_handler(message):
    bot_user = User.objects.get(user_id=message.from_user.id)
    bot_elon = Elon.objects.get(user=bot_user, active=False)
    if bot_elon.step == 12:
        raw = message.photo[1].file_id
        path = raw + ".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        content = ContentFile(downloaded_file)
        bot_elon.image.save(path, content, save=True)
        bot_elon.step = 13
        bot_elon.save()
        bot.send_message(message.from_user.id, "<b>2️⃣Keyingi rasmni yuboring</b>")
    elif bot_elon.step == 13:
        raw = message.photo[1].file_id
        path = raw + ".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        content = ContentFile(downloaded_file)
        bot_elon.image1.save(path, content, save=True)
        bot_elon.step = 14
        bot_elon.save()
        bot.send_message(message.from_user.id, "<b>3️⃣So`nggi rasmni yuboring</b>")
    elif bot_elon.step == 14:
        raw = message.photo[1].file_id
        path = raw + ".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        content = ContentFile(downloaded_file)
        bot_elon.image2.save(path, content, save=True)
        bot_elon.step = 15
        bot_elon.save()
        bot.send_message(message.from_user.id, "<b>☑️Rasmar muvaffaqiyatli yuklandi</b>", reply_markup=hideBoard)
        text = f"<u><b>📋E`loningiz ma`lumotlari:</b></u>\n<b>👉Elon turi:</b> <i>{bot_elon.category}</i>.\n👤<b>Ism:</b> <i>{bot_elon.first_name}.</i>\n📞<b>Tel raqam:</b> <i>{bot_elon.phone_number}.</i>\n<b>🏠Manzil:</b> <i>{bot_elon.address}</i>.\n 🚘<b>Nomi:</b> <i>{bot_elon.model}</i>.\n⚙️<b>Yili:</b> <i>{bot_elon.year}</i>.\n🐎<b>Probegi:</b> <i>{bot_elon.journey} km</i>.\n📁<b>Yuridik holati:</b> <i>{bot_elon.policy}.</i> \n⏫<b>Korobka:</b> <i>{bot_elon.korobka}</i>.\n⛽️<b>Yonilg`i:</b> <i>{bot_elon.fuel}</i>.\nℹ️<b>Qo`shimcha:</b> <i>{bot_elon.comment}</i>\n💸<b>Narxi:</b> <i>{bot_elon.price} ￦</i> \n\n<i>Bizning kanalga a`zo bo`ling: https://t.me/korea_elonlar\nE`lon berish uchun: https://t.me/korea_savdo_bot</i>"
        bot.send_media_group(chat_id=message.from_user.id,
                             media=[InputMediaPhoto(bot_elon.image, caption=text, parse_mode="HTML"),
                                    InputMediaPhoto(bot_elon.image1),
                                    InputMediaPhoto(bot_elon.image2)])
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn = types.InlineKeyboardButton('✅OK', callback_data='ok')
        btn1 = types.InlineKeyboardButton('♻️Qayta to`ldirish', callback_data='cancel')
        markup.add(btn, btn1)
        bot.send_message(message.from_user.id,
                         "<i>Ma`limotlaringiz barchasi to`g`ri bo`lsa 'OK' tugmasini bosing va e`loningiz Adminga yuboriladi!</i>",
                         reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def call_data(call):
    if call.data == "ok":
        bot_user = User.objects.get(user_id=call.from_user.id)
        bot_elon = Elon.objects.get(user=bot_user, active=False)
        bot_elon.active = True
        bot_elon.step = 16
        bot_elon.save()
        text = f"<u><b>📋E`lon ma`lumotlari:</b></u>\n<b>👉Elon turi:</b> <i>{bot_elon.category}</i>.\n👤<b>Ism:</b> <i>{bot_elon.first_name}.</i>\n📞<b>Tel raqam:</b> <i>{bot_elon.phone_number}.</i>\n<b>🏠Manzil:</b> <i>{bot_elon.address}</i>.\n 🚘<b>Nomi:</b> <i>{bot_elon.model}</i>.\n⚙️<b>Yili:</b> <i>{bot_elon.year}</i>.\n🐎<b>Probegi:</b> <i>{bot_elon.journey} km</i>.\n📁<b>Yuridik holati:</b> <i>{bot_elon.policy}.</i> \n⏫<b>Korobka:</b> <i>{bot_elon.korobka}</i>.\n⛽️<b>Yonilg`i:</b> <i>{bot_elon.fuel}</i>.\nℹ️<b>Qo`shimcha:</b> <i>{bot_elon.comment}</i>\n💸<b>Narxi:</b> <i>{bot_elon.price} ￦</i> \n"
        bot.send_media_group(chat_id=-676703746,
                             media=[InputMediaPhoto(bot_elon.image, caption=text, parse_mode="HTML"),
                                    InputMediaPhoto(bot_elon.image1),
                                    InputMediaPhoto(bot_elon.image2)])
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('🔰Yordam')
        btn1 = types.KeyboardButton('🚘Avtomobil')
        btn2 = types.KeyboardButton('📄E`lonlarim')
        # btn2 = types.KeyboardButton('Telefon')
        # btn3 = types.KeyboardButton('Notebook')
        markup.add(btn1, btn, btn2)
        bot.send_message(call.from_user.id,
                         "<b>✅E`loningiz Adminga yuborildi va tez orada elon ko`rib chiqiladi. Admin nazoratidan o`tganidan so`ng: https://t.me/korea_elonlar kanaliga yuklanadi\nYangi e`lon berish uchun e`lon turini tanlang</b>",
                         reply_markup=markup)
        bot_user = User.objects.get(user_id=call.from_user.id)
        elon = Elon.objects.create(
            user=bot_user
        )
        elon.save()

    elif call.data == 'cancel':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = types.KeyboardButton('🔰Yordam')
        btn1 = types.KeyboardButton('🚘Avtomobil')
        btn2 = types.KeyboardButton('📄E`lonlarim')
        # btn2 = types.KeyboardButton('Telefon')
        # btn3 = types.KeyboardButton('Notebook')
        markup.add(btn1, btn, btn2)
        bot.send_message(call.from_user.id, "<b>✅E`lon bekor qilindi!\nE`lon turini tanlang!</b>", reply_markup=markup)
        bot_user = User.objects.create(user_id=call.from_user.id, username=call.from_user.username)
        bot_user.save()
        elon = Elon.objects.create(
            user=bot_user
        )
        elon.save()

    print('ureeeeeeeee')
