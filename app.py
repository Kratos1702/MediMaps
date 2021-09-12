"""
        MEDI COVID MAPS BOT
    cr: Marcello Esposito 5°Ei
       mespositow@gmail.com
"""

import logging

from telegram import InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from com import kb_vars, msg_default
from com.misc import send_msg
from com.tasks.base_tasks import do_base_tasks
from com.tasks.enter_tasks import do_enter_tasks
from com.tasks.exit_tasks import do_exit_tasks
from com.tasks.move_tasks import do_move_tasks

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context, isFirst=True):
    reply_markup = InlineKeyboardMarkup(kb_vars.BASE_KB)
    first_name = update.message.from_user['first_name'] if isFirst else update.message.chat['first_name']
    msg = msg_default.WELCOME_MSG.format(first_name)
    send_msg(update, msg, reply_markup)


def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    # INITIAL OPT HANDLER
    if "base" in query.data:
        do_base_tasks(query)
    elif "mov" in query.data:
        do_move_tasks(query)
    elif "ent" in query.data:
        do_enter_tasks(query)
    elif "ex" in query.data:
        do_exit_tasks(query)
    elif "start" in query.data:
        start(query, "_", False)


def help_command(update, context):
    reply_markup = InlineKeyboardMarkup(kb_vars.PRESS_HERE_KB)
    send_msg(update, msg_default.HELP_MSG, reply_markup)


def credits_command(update, context=""):
    reply_markup = InlineKeyboardMarkup(kb_vars.CREDITS_KB)
    send_msg(update, msg_default.CREDITS_MSG, reply_markup)


def main():
    try:
        # Create the Updater and pass it your bot's token.
        # use_context=True allow callbacks
        updater = Updater("INSERT TOKEN HERE", use_context=True)

        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(CallbackQueryHandler(button))  # Active callback on btns
        updater.dispatcher.add_handler(CommandHandler('help', help_command))
        updater.dispatcher.add_handler(CommandHandler('credits', credits_command))

        # Start the Bot
        updater.start_polling()

        # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
        updater.idle()
    except Exception:
        pass


if __name__ == '__main__':
    main()
