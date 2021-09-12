from telegram import InlineKeyboardMarkup

from com import msg_default, kb_vars


def new_line(query, section):
    msg = msg_default.NEW_LINE_MSG.format(section)
    send_msg(query, msg)


def restart(query):
    reply_markup = InlineKeyboardMarkup(kb_vars.BASE_KB)
    msg = msg_default.RESTART_MSG.format(query.from_user['first_name'])
    query.message.reply_text(msg, reply_markup=reply_markup)


def send_msg(query, msg, kb=None):
    if not kb:
        query.message.reply_text(msg)
    else:
        query.message.reply_text(msg, reply_markup=kb)


def send_img(query, img_url):
    query.message.reply_photo(img_url)


def send_doc(query, file_url):
    query.message.reply_document(file_url)
