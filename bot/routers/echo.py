from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from django.utils.translation import gettext_lazy as _, activate
from app.users.models import TelegramUser as User
from bot.utils.kbs import menu_keyboards_dict

router = Router()


@router.message()
async def echo_handler(message: types.Message, user: User) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like text, photo, sticker etc.)
    """
    menu_text_list = [menu for emoji_list in menu_keyboards_dict.values() for menu in emoji_list]
    activate(user.language)

    if message.text in menu_text_list:
        if message.text in ("🍟 Заказать", "🍟 Buyurtma berish"):
            await message.answer(
                "Good. Now you can try to send it via Webview",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="Open Webview",
                                web_app=WebAppInfo(url="https://warm-centrally-mutt.ngrok-free.app/telegram")
                            )
                        ]
                    ]
                ),
            )

