from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, LabeledPrice, PreCheckoutQuery
from django.conf import settings
from django.utils.translation import gettext_lazy as _, activate

from app.address.models import Address, Branch
from app.users.models import TelegramUser as User
from bot.functions import get_location_name_async
from bot.utils.kbs import menu_keyboards_dict, menu_kb
from app.products.models import Order

router = Router()


@router.message(F.successful_payment)
async def echo_successfull_payment(message: types.Message, user: User) -> None:
    try:
        order = await Order.objects.aget(pk=int(message.successful_payment.invoice_payload))
        order.status = order.STATUS.PAID
        order.charge_id = message.successful_payment.provider_payment_charge_id
        await order.asave()
    except Order.DoesNotExist:
        ...


@router.pre_checkout_query()
async def echo_checkout(query: PreCheckoutQuery):
    """
    id='8187792719859100214' from_user=User(id=6201336345, is_bot=False, first_name='Gayrat', last_name='Sultonov',
    username=None, language_code='ru', is_premium=None, added_to_attachment_menu=None,
    can_join_groups=None, can_read_all_group_messages=None, supports_inline_queries=None)
    currency='UZS' total_amount=10000 invoice_payload='tttt' shipping_option_id=None order_info=None
    """
    try:
        order = await Order.objects.aget(pk=int(query.invoice_payload))
        if order.status == order.STATUS.CREATED:
            await query.bot.answer_pre_checkout_query(query.id, ok=True)
            return
        error_message = str(_("Savat allaqachon to'langan"))
    except Order.DoesNotExist:
        error_message = str(_("Savat topilmadi"))
    await query.bot.answer_pre_checkout_query(query.id, ok=False, error_message=error_message)


@router.message()
async def echo_handler(message: types.Message, user: User) -> None:
    text = str(_("Bo'limni tanlang"))
    menu_text_list = [menu for emoji_list in menu_keyboards_dict.values() for menu in emoji_list]
    activate(user.language)

    if message.text in menu_text_list:
        if message.text in ("🍟 Заказать", "🍟 Buyurtma berish"):
            url = settings.HOST + "/tg/?lang=" + user.language
            await message.answer(
                str(_("Buyurtma berish uchun quyidagi tugmani bosing")),
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text=message.text,
                                web_app=WebAppInfo(url=url)
                            )
                        ]
                    ]
                ),
            )
        elif message.text in ("🏠 Filiallar", "🏠 Филиалы"):
            counter = 1
            branches = Branch.objects.filter(is_active=True)
            branches_text = str(_("🏡 Filiallar\n\n"))
            async for filial in branches:
                branches_text += str(counter) + ". " + filial.name + "\n"
                counter += 1
            await message.answer(branches_text)
        elif message.text in ("🏡 Manzillarim", "🏡 Мои адреса"):
            counter = 1
            addresses = Address.objects.filter(user=user)
            address_text = str(_("🏡 Manzillarim\n\n"))
            async for address in addresses:
                address_text += str(counter) + ". " + address.name + "\n"
                counter += 1
            await message.answer(address_text)
    elif message.location:
        name = await get_location_name_async(message.location.latitude, message.location.longitude)
        await Address.objects.aupdate_or_create(
            user=user, name=name, defaults={"longitude": message.location.longitude,
                                            "latitude": message.location.latitude}
        )
        await message.answer(text, reply_markup=menu_kb(user.language))
    else:
        await message.answer(text, reply_markup=menu_kb(user.language))
