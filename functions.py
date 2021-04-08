

import datetime

import messages as msg

import markups as mrk

from telegram.constants import CHATACTION_TYPING

import time


def start(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = msg.hello.format(first_name.capitalize())
    context.bot.send_message(chat_id=chat_id,
                             text=text,
                             reply_markup=mrk.languages())

def text_msg(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = update.message.text.lower()
    if text == '🇷🇺русский':
        context.bot.send_message(chat_id, '.', reply_markup=mrk.ReplyKeyboardRemove())
        context.bot.delete_message(chat_id, update.message.message_id+1)
        context.bot.send_message(chat_id=chat_id,
                                 reply_markup=mrk.main_menu(),
                                 text='No онгличанс!')
    else:
        context.bot.send_message(chat_id=chat_id,
                                 text='1')

def inline_reply(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    time.sleep(0.5)
    context.bot.send_message(chat_id=chat_id,
                             text="Какая достопримечательность вас интересует ?",
                             reply_markup=mrk.places())
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)

def places_to_go(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    time.sleep(0.5)
    context.bot.send_message(chat_id=chat_id,
                             text="Места куда можно сходить: ",
                             reply_markup=mrk.places())
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)

def registan(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    time.sleep(0.5)
    context.bot.send_message(chat_id=chat_id,
                             text=msg.ab_registan,
                             reply_markup=mrk.back())
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)
def guremir(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    time.sleep(0.5)
    context.bot.send_message(chat_id=chat_id,
                             text=msg.ab_guremir,
                             reply_markup=mrk.back())
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)

def bibh(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    time.sleep(0.5)
    context.bot.send_message(chat_id=chat_id,
                             text=msg.ab_bibh,
                             reply_markup=mrk.back())
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)

def ulug(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    time.sleep(0.5)
    context.bot.send_message(chat_id=chat_id,
                             text=msg.ab_ulug,
                             reply_markup=mrk.back())
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)

def shah(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    time.sleep(0.5)
    context.bot.send_message(chat_id=chat_id,
                             text=msg.ab_shah,
                             reply_markup=mrk.back())
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)

def afr(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    time.sleep(0.5)
    context.bot.send_message(chat_id=chat_id,
                             text=msg.ab_afr,
                             reply_markup=mrk.back())
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)


def smk_back(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    time.sleep(0.5)
    context.bot.send_message(chat_id=chat_id,
                             reply_markup=mrk.main_menu(),
                             text='Что вы хотите узнать ?')
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)

def smk(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    time.sleep(0.5)
    context.bot.send_message(chat_id=chat_id,
                             text=msg.ab_smk,
                             reply_markup=mrk.back())
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)
