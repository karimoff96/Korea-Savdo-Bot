import telebot
from telebot import types
from .models import *

bot = telebot.TeleBot('5176543389:AAHidLypZBK6qzGlnlWJdT71eShOcwEANxE', parse_mode="HTML")


class Controller:
    def __init__(self, m, userid, messageid=None, call_data=None, chatid=None):
        self.userid = userid
        self.messageid = messageid
        self.call_data = call_data
        self.chatid = chatid
        self.m = m

    def cat(self):
        category = Category.objects.all()
        ikey = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        l = len(category)
        print(category, l)
        for i in range(0, l, 2):
            btn = types.KeyboardButton(f'{category[i].name}')
            if l % 2 == 1 and l - 1 == i:
                ikey.add(btn)
            else:
                btn1 = types.KeyboardButton(f'{category[i + 1].name}')
                ikey.add(btn, btn1)
            bot.send_message(self.userid, '<b>Kategoriyani tanlang</b>', reply_markup=ikey, parse_mode='HTML')
