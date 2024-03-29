from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from app.handlers.handlers_commands import admin_commands


add_color = KeyboardButton(f'{admin_commands["Додати_пігмент"]}')
delete_creator = KeyboardButton(f'{admin_commands["Видалити_виробника"]}')
add_creator = KeyboardButton(f'{admin_commands["Додати_виробника"]}')
make_newsletter = KeyboardButton(f'{admin_commands["Зробити_розсилку"]}')
cancel = KeyboardButton(f'{admin_commands["Відмінити"]}')

manager_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

manager_keyboard.add(add_color).add(make_newsletter).add(add_creator).insert(delete_creator)


def cancel_markup_admin():
    cancel_mark = ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_button = KeyboardButton(f'{admin_commands["Відмінити"]}')
    return cancel_mark.add(cancel_button)


choose_manager_keyboard = KeyboardButton(f'/{admin_commands["Клавіатура_менеджера"]}')
choose_client_keyboard = KeyboardButton(f'/{admin_commands["Клавіатура_клієнта"]}')


choose_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

choose_keyboard.add(choose_manager_keyboard).add(choose_client_keyboard)
