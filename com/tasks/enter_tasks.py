"""
        MEDI COVID MAPS BOT
    cr: Marcello Esposito 5Â°Ei
       mespositow@gmail.com
"""

from com import msg_default
from com.misc import restart, send_msg, send_img

text_list = [
    "ð¸ Utilizzare l'ingresso 'Rampa centrale D'",
    "ð¸ Utilizzare l'ingresso 'A'",
    "ð¸ Utilizzare l'ingresso 'F'",
    "ð¸ Utilizzare l'ingresso 'G'",
    "ð¸ Utilizzare l'ingresso 'I'",
    "ð¸ 1Â° ora: Utilizzare l'ingresso 'R1'\nð¸ 2Â° ora: Utilizzare l'ingresso 'D'",
    "ð¸ 1Â° ora: Utilizzare l'ingresso 'R2'\nð¸ 2Â° ora: Utilizzare l'ingresso 'D'",
    "ð¸ Utilizzare l'ingresso 'D'"
]


def do_enter_tasks(query):
    if "1" in query.data:
        send_enter(query, 0)
    elif "2" in query.data:
        send_enter(query, 1)
    elif "3" in query.data:
        send_enter(query, 2)
    elif "4" in query.data:
        send_enter(query, 3)
    elif "5" in query.data:
        send_enter(query, 4)
    elif "6" in query.data:
        send_enter(query, 5)
    elif "7" in query.data:
        send_enter(query, 6)
    elif "8" in query.data:
        send_enter(query, 7)


def send_enter(query, index):
    img = "http://enricomeditest.altervista.org/bot/img/ent/full_map.PNG"
    send_msg(query, text_list[index])
    try:
        send_img(query, img)
    except Exception:
        send_msg(query, msg_default.ISSUE_FILE_MSG)

    send_msg(query, msg_default.DANGER_MSG)

    restart(query)
