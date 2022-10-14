import telebot

from keyboards import sub, notsub
from config import TOKEN, channel_id1, channel_id2, NOT_SUB_MESSAGE, YES_SUB_MESSAGE


bot = telebot.TeleBot(TOKEN)


def check_sub_channel(chat_member):
    if chat_member.status != 'left':
        return True
    else:
        return False


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        if check_sub_channel(bot.get_chat_member(chat_id=channel_id1, user_id=message.from_user.id))\
            and check_sub_channel(bot.get_chat_member(chat_id=channel_id2, user_id=message.from_user.id)):
                bot.send_message(message.from_user.id, YES_SUB_MESSAGE, reply_markup=sub)
        else:
            bot.send_message(message.from_user.id, NOT_SUB_MESSAGE, reply_markup=notsub)


@bot.callback_query_handler(func=lambda call: True)
def query(call):
    if call.data == 'subscribed':
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        if check_sub_channel(bot.get_chat_member(chat_id=channel_id1, user_id=call.from_user.id))\
            and check_sub_channel(bot.get_chat_member(chat_id=channel_id2, user_id=call.from_user.id)):
                bot.send_message(call.from_user.id, YES_SUB_MESSAGE, reply_markup=sub)         
        else:
            bot.send_message(call.from_user.id, NOT_SUB_MESSAGE, reply_markup=notsub)

bot.polling(non_stop=True)