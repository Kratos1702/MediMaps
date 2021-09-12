"""
        MEDI COVID MAPS BOT
    cr: Marcello Esposito 5°Ei
       mespositow@gmail.com
"""

from telegram import InlineKeyboardButton

# start kb
BASE_KB_CB = ['base_mov', 'base_ent', 'base_ex', 'base_map', 'base_stop']
BASE_KB = [
    [InlineKeyboardButton("⚪️ Cambio", callback_data=BASE_KB_CB[0]),
     InlineKeyboardButton("🟠  Entrata", callback_data=BASE_KB_CB[1]),
     InlineKeyboardButton("🔵   Uscita", callback_data=BASE_KB_CB[2])],
    [InlineKeyboardButton("🟢  Mappa completa e regolamento", callback_data=BASE_KB_CB[3])],
    [InlineKeyboardButton("🟣  Niente, grazie", callback_data=BASE_KB_CB[4]),
     InlineKeyboardButton("🔴   Segnala un errore", url="tg://resolve?domain=Marcello02")]
]


test_kb = [
    []
]
# movement kb
MOVE_KB_CB = ['mov_1', 'mov_2', 'mov_3', 'mov_4', 'mov_5', 'mov_6', 'mov_7']
MOVE_KB = [
    [InlineKeyboardButton("Aule: 01 a 05 (ex-ced)", callback_data=MOVE_KB_CB[0])],
    [InlineKeyboardButton("Aule: 06 a 12", callback_data=MOVE_KB_CB[1])],
    [InlineKeyboardButton("Lab: 15 a 26. Aule: Pesiri, Muto", callback_data=MOVE_KB_CB[2])],
    [InlineKeyboardButton("Aule: 106 a 108", callback_data=MOVE_KB_CB[3])],
    [InlineKeyboardButton("Lab: 09, 27 a 29. Aule: 122, E01 a E04, Campus", callback_data=MOVE_KB_CB[4])],
    [InlineKeyboardButton("Lab: 01 a 07, 11, 12. Aule: E014, 120, 126", callback_data=MOVE_KB_CB[5])],
    [InlineKeyboardButton("Aule 1° a 5° livello", callback_data=MOVE_KB_CB[6])]
]

# enter kb
ENTER_KB_CB = ['ent_1', 'ent_2', 'ent_3', 'ent_4', 'ent_5', 'ent_6', 'ent_7', 'ent_8']
ENTER_KB = [
    [InlineKeyboardButton("Aule: 01 a 05 (ex-ced)", callback_data=ENTER_KB_CB[0])],
    [InlineKeyboardButton("Aule: 06 a 12", callback_data=ENTER_KB_CB[1])],
    [InlineKeyboardButton("Lab: 15 a 26. Aula: Pesiri, Muto, 106 a 108", callback_data=ENTER_KB_CB[2])],
    [InlineKeyboardButton("Lab: 09, 27 a 29. Aule: 122, E01 a E04, Campus", callback_data=ENTER_KB_CB[3])],
    [InlineKeyboardButton("Lab: 01 a 07, 11, 12. Aule: E014, 120, 126", callback_data=ENTER_KB_CB[4])],
    [InlineKeyboardButton("Aule 1° livello", callback_data=ENTER_KB_CB[5])],
    [InlineKeyboardButton("Aule 2° livello", callback_data=ENTER_KB_CB[6])],
    [InlineKeyboardButton("Aule 3°, 4°, 5° livello", callback_data=ENTER_KB_CB[7])]
]

# exit kb
EXIT_KB_CB = ['ex_1', 'ex_2', 'ex_3', 'ex_4', 'ex_5', 'ex_6', 'ex_7', 'ex_8', 'ex_9', 'ex_10']
EXIT_KB = [
    [InlineKeyboardButton("Aule: 01 a 05 (ex-ced)", callback_data=EXIT_KB_CB[0])],
    [InlineKeyboardButton("Aule: 06 a 12", callback_data=EXIT_KB_CB[1])],
    [InlineKeyboardButton("Aule: Campus", callback_data=EXIT_KB_CB[2])],
    [InlineKeyboardButton("Palestra", callback_data=EXIT_KB_CB[3])],
    [InlineKeyboardButton("Lab: Chimica", callback_data=EXIT_KB_CB[4])],
    [InlineKeyboardButton("Lab: Elettrotecnica", callback_data=EXIT_KB_CB[5])],
    [InlineKeyboardButton("Aule 1° livello", callback_data=EXIT_KB_CB[6])],
    [InlineKeyboardButton("Aule 2° livello", callback_data=EXIT_KB_CB[7])],
    [InlineKeyboardButton("Aule 3° livello", callback_data=EXIT_KB_CB[8])],
    [InlineKeyboardButton("Aule 4°, 5° livello", callback_data=EXIT_KB_CB[9])]
]

# press_here kb
PRESS_HERE_KB = [[InlineKeyboardButton("👉  PREMI QUI  👈", callback_data="start")]]

# credits kb
CREDITS_KB = [
    [InlineKeyboardButton("✉️ Email", url="https://kratos.altervista.org/page2.html#header6-p")],
    [InlineKeyboardButton("📱 Telegram", url="tg://resolve?domain=Marcello02")],
    [InlineKeyboardButton("❌ Torna dietro", callback_data="start")]
]
