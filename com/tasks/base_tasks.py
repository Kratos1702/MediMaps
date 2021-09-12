"""
        MEDI COVID MAPS BOT
    cr: Marcello Esposito 5°Ei
       mespositow@gmail.com
"""

import telegram
from telegram import InlineKeyboardMarkup

from com import msg_default
from com import kb_vars
from com.misc import new_line, restart, send_doc, send_msg


def do_base_tasks(query):
    task_list = kb_vars.BASE_KB_CB
    if query.data == task_list[0]:  # movement
        movement_t(query)
    elif query.data == task_list[1]:  # enter
        enter_t(query)
    elif query.data == task_list[2]:  # exit
        exit_t(query)
    elif query.data == task_list[3]:  # map
        map_t(query)
    elif query.data == task_list[4]:  # stop
        stop_t(query)


def movement_t(query):
    reply_markup = InlineKeyboardMarkup(kb_vars.MOVE_KB)

    new_line(query, "SPOSTAMENTI")
    send_msg(query, "Dove ti trovi?", reply_markup)


def enter_t(query):
    reply_markup = InlineKeyboardMarkup(kb_vars.ENTER_KB)

    new_line(query, "INGRESSO")
    send_msg(query, "Dove devi arrivare?", reply_markup)


def exit_t(query):
    reply_markup = InlineKeyboardMarkup(kb_vars.EXIT_KB)

    new_line(query, "USCITA")
    send_msg(query, "Dove ti trovi?", reply_markup)


def map_t(query):
    new_line(query, "MAPPA")
    try:
        send_doc(query, "https://enricomeditest.altervista.org/bot/mappa.pdf")
        send_doc(query, "https://enricomeditest.altervista.org/bot/percorsi.pdf")
        send_doc(query, "https://enricomeditest.altervista.org/bot/Regolamento.pdf")
    except Exception:
        send_msg(query, msg_default.ISSUE_FILE_MSG)

    restart(query)


def stop_t(query):
    msg = msg_default.CLOSE_MSG.format(query.from_user['first_name'])
    send_msg(query, msg)
