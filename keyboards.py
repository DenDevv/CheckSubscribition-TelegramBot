from telebot import types

notsub = types.InlineKeyboardMarkup(row_width=2)
notsub.add(types.InlineKeyboardButton('I subscribed ✅', callback_data='subscribed'))

sub = types.InlineKeyboardMarkup(row_width=2)
sub.add(types.InlineKeyboardButton('See 🎥', url=''))