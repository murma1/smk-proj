from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        for i in footer_buttons:
            menu.append([i])
    return menu


def languages():
    button_list = [
             KeyboardButton("🇷🇺Русский"),
             KeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿󠁧󠁢󠁥󠁮󠁧English")
    ]

    return ReplyKeyboardMarkup([[button_list[0]],
                               [button_list[1]]], resize_keyboard=True,one_time_keyboard=True)

def main_menu():
    button_list = [
        InlineKeyboardButton("Куда можно сходить ?", callback_data='places'),
        InlineKeyboardButton("Информация о достопримечательности", callback_data='yes'),
        InlineKeyboardButton("Про Самарканд", callback_data='smk')
    ]
    return InlineKeyboardMarkup(build_menu(button_list, 1))

def places():
    button_list = [
        InlineKeyboardButton("Регистан", callback_data='registan'),
        InlineKeyboardButton("Гур Эмир", callback_data='guremir'),
        InlineKeyboardButton("Биби-Ханум", callback_data='bibh'),
        InlineKeyboardButton("Обсерватория Улугбека", callback_data='ulug'),
        InlineKeyboardButton("Шахи-Зинда", callback_data='shah'),
        InlineKeyboardButton("Музей 'Афросиаб'", callback_data='afr'),
        InlineKeyboardButton("⬅️Назад", callback_data='back')
        ]

    return InlineKeyboardMarkup(build_menu(button_list, 2))

def back():
    button_list = [
        InlineKeyboardButton("⬅️Назад", callback_data='smk_back')
        ]

    return InlineKeyboardMarkup(build_menu(button_list, 1))


