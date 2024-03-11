from aiogram.utils.keyboard import ReplyKeyboardBuilder
from django.utils.translation import gettext_lazy as _
from aiogram.types import KeyboardButton, KeyboardButtonRequestChat, KeyboardButtonRequestUsers

languages = (
    str(_("🇺🇿 O'zbek tili")),
    str(_("🇷🇺 Русский язык"))
)
menu_keyboards_dict = {
    "ru": ("🍟 Заказать", "🏠 Filiallar", "🏡 Manzillarim"),
    "uz": ("🍟 Buyurtma berish", "🏠 Филиалы", "🏡 Мои адреса")
}
send_location_text = str(_("Lokasiya yuborish"))


def contact_kb():
    markup = ReplyKeyboardBuilder()
    markup.add(KeyboardButton(text=str(_("Отправить телефон")), request_contact=True))
    return markup.adjust(2).as_markup(resize_keyboard=True)


def location_kb():
    markup = ReplyKeyboardBuilder()
    markup.add(KeyboardButton(text=send_location_text, request_location=True))
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
    markup.add(
        KeyboardButton(text=send_location_text, request_location=True)
    )
    return markup.adjust(2).as_markup(resize_keyboard=True)
