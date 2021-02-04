import os
import sys
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence, CallbackQueryHandler
from api.handlers import get_k_items, get_full_job_text, start

if __name__ == '__main__':
    ACCESS_TOKEN = os.environ['JOB_FINDER_TOKEN']
    updater = Updater(token=ACCESS_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(get_full_job_text))
    dispatcher.add_handler(MessageHandler(Filters.text, get_k_items
                                          ))


    updater.start_polling()
