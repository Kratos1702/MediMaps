"""
        MEDI COVID MAPS BOT
    cr: Marcello Esposito 5°Ei
       mespositow@gmail.com
"""

from com import kb_vars, msg_default
from com.misc import restart, send_msg, send_img

text_list = [
    "Dirigersi verso l’acquario per recarsi:\n◽️ al laboratorio 01\n◽️ in palestra utilizzando la scala " \
    "centrale e procedendo verso l’uscita lato archivio (P).\n◽️ ai vari laboratori utilizzando la rampa " \
    "interna per accedere al secondo livello alla fine della quale prendere la rampa esterna proseguendo verso " \
    "R2:\n\t\t▫️ l’ingresso (F) per accedere ai laboratori 15 a 26\n\t\t▫️ l’ingresso (I) per accedere ai " \
    "laboratori 02 a 05, E06, 07, 11, 12\n\t\t▫️ l’ingresso (G) per accedere ai laboratori 09. 27, 28, 29. ",

    "Prendere l'uscita cancello lato archivio(P) per recarsi:\n◽️ In palestra\n◽️ Alle entrate indicate dei vari "
    "laboratori",

    "Seguire i percorsi covid ed uscire da ingresso H per recarsi:\n◽️ in palestra dall'esterno\n◽️ alle aule "
    "rientrando dall'ingresso I\n◽️ ad ulteriori laboratori ",

    "Uscire per il corridoio stretto e dirigersi verso la scala centrale per recarsi:\n◽️ In palestra\n◽️ nei "
    "laboratori procedendo verso l'uscita lato archivio (P) passando per l'esterno ",

    "Uscire dal cancello H ed utilizzare:\n◽️ ingresso elettrotecnica I per recarsi nelle aule ai livelli e per "
    "recarsi alle aule campus\n◽️ percorso esterno per recarsi in palestra.",

    "Uscita corridoio verso rampe centrali per recarsi:\n◽️ nelle aule ai livelli\n◽️ in palestra utilizzando la "
    "scala centrale e procedendo verso l’uscita lato archivio (P).",

    "Ingresso palestra\n◽️ entrata in palestra lato campetto esterno (E)",
]


def do_move_tasks(query):
    if "1" in query.data:
        send_mov(query, 0)
    elif "2" in query.data:
        send_mov(query, 1)
    elif "3" in query.data:
        send_mov(query, 2)
    elif "4" in query.data:
        send_mov(query, 3)
    elif "5" in query.data:
        send_mov(query, 4)
    elif "6" in query.data:
        send_mov(query, 5)
    elif "7" in query.data:
        send_mov(query, 6)


def send_mov(query, index):
    img = "mov_" + str(index + 1)
    url = "http://enricomeditest.altervista.org/bot/img/mov/" + img
    if index != 6:
        url = url + ".PNG"
    else:
        url = url + ".png"

    send_msg(query, text_list[index])
    try:
        send_img(query, url)
    except Exception:
        send_msg(query, msg_default.ISSUE_FILE_MSG)

    send_msg(query, msg_default.DANGER_MSG)

    restart(query)
