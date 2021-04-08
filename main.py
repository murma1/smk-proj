
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters

from const import API_TOKEN

from functions import *

updater = Updater(token=API_TOKEN, workers=8)

dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler('start',
                                      start))


dispatcher.add_handler(MessageHandler(Filters.text,
                                      text_msg))


dispatcher.add_handler((CallbackQueryHandler(callback=inline_reply,
                                             pattern='yes')))

dispatcher.add_handler((CallbackQueryHandler(callback=places_to_go,
                                             pattern='places')))

dispatcher.add_handler((CallbackQueryHandler(callback=registan,
                                             pattern='registan')))

dispatcher.add_handler((CallbackQueryHandler(callback=guremir,
                                             pattern='guremir')))

dispatcher.add_handler((CallbackQueryHandler(callback=bibh,
                                             pattern='bibh')))

dispatcher.add_handler((CallbackQueryHandler(callback=ulug,
                                             pattern='ulug')))

dispatcher.add_handler((CallbackQueryHandler(callback=shah,
                                             pattern='shah')))

dispatcher.add_handler((CallbackQueryHandler(callback=afr,
                                             pattern='afr')))

dispatcher.add_handler((CallbackQueryHandler(callback=smk_back,
                                             pattern='smk_back')))

dispatcher.add_handler((CallbackQueryHandler(callback=smk_back,
                                             pattern='back')))


dispatcher.add_handler((CallbackQueryHandler(callback=smk,
                                             pattern='smk')))

updater.start_polling()

updater.idle()
