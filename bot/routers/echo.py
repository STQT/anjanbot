from aiogram import Router, types
from django.utils.translation import gettext_lazy as _, activate
from app.users.models import TelegramUser as User

router = Router()


@router.message()
async def echo_handler(message: types.Message, user: User) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like text, photo, sticker etc.)
    """
    await message.answer(_("Hello"))
