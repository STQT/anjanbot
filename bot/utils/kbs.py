from aiogram.utils.keyboard import ReplyKeyboardBuilder
from django.utils.translation import gettext_lazy as _
from aiogram.types import KeyboardButton, KeyboardButtonRequestChat, KeyboardButtonRequestUsers

languages = (
    str(_("🇺🇿 O'zbek tili")),
    str(_("🇷🇺 Русский язык"))
)
menu_keyboards_dict = {
    "ru": ("🍟 Заказать",),
    "uz": ("🍟 Buyurtma berish",)
}


def contact_kb():
    markup = ReplyKeyboardBuilder()
    markup.add(KeyboardButton(text=str(_("Отправить телефон")), request_contact=True))
    return markup.adjust(2).as_markup(resize_keyboard=True)


def language_kb():
    markup = ReplyKeyboardBuilder()
    markup.add(
        *(KeyboardButton(text=lang) for lang in languages)
    )
    return markup.adjust(2).as_markup(resize_keyboard=True)


def menu_kb(language_code='ru'):
    markup = ReplyKeyboardBuilder()
    markup.add(
        *(KeyboardButton(text=menu) for menu in menu_keyboards_dict[language_code])
    )
    return markup.adjust(2).as_markup(resize_keyboard=True)
