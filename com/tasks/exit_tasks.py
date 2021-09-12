"""
        MEDI COVID MAPS BOT
    cr: Marcello Esposito 5°Ei
       mespositow@gmail.com
"""

from com import kb_vars, msg_default
from com.misc import restart, send_msg, send_img

text_list = [
    "Utilizzare nell’ordine:\n🔹 uscita lato archivio (P)\n🔹 cancello parcheggio",

    "Utilizzare nell’ordine:\n🔹 uscita lato caldaia campus uscita H\n🔹 cancello parcheggi",

    "Utilizzare nell’ordine:\n🔹 uscita h\n🔹 cancello parcheggi",

    "Utilizzare nell’ordine:\n🔹 campetto esterno\n🔹 cancello parcheggi",

    "Utilizzare nell’ordine:\n🔹 rampa di uscita ex ced (D)\n🔹 cancello principale",

    "Utilizzare nell’ordine:\n🔹 uscita ex-ced (D)\n🔹 cancello principale",

    "Utilizzare nell’ordine:\n🔹 rampa R1\n🔹 cancello parcheggi",

    "Utilizzare nell’ordine:\n🔹 rampa uscita emergenza lato chimica (R2)\n🔹 cancello principale",

    "Utilizzare nell’ordine:\n🔹 scale emergenza\n🔹 rampa R1\n🔹 cancello parcheggi",

    "Utilizzare nell’ordine:\n🔹 rampa uscita emergenza lato chimica (R2)\n🔹 cancello principale"
]


def do_exit_tasks(query):
    if "10" in query.data:
        send_ex(query, 9)
    elif "1" in query.data:
        send_ex(query, 0)
    elif "2" in query.data:
        send_ex(query, 1)
    elif "3" in query.data:
        send_ex(query, 2)
    elif "4" in query.data:
        send_ex(query, 3)
    elif "5" in query.data:
        send_ex(query, 4)
    elif "6" in query.data:
        send_ex(query, 5)
    elif "7" in query.data:
        send_ex(query, 6)
    elif "8" in query.data:
        send_ex(query, 7)
    elif "9" in query.data:
        send_ex(query, 8)


def send_ex(query, index):
    img = "ex_" + str(index + 1)
    url = "http://enricomeditest.altervista.org/bot/img/ex/" + img + ".PNG"

    send_msg(query, text_list[index])

    if index != 3:
        try:
            print(url)
            send_img(query, url)
        except Exception:
            send_msg(query, msg_default.ISSUE_FILE_MSG)

    send_msg(query, msg_default.DANGER_MSG)

    restart(query)
