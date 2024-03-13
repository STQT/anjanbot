from aiogram import Router, types, F
from aiogram.types import PreCheckoutQuery
from django.utils.translation import gettext_lazy as _

from app.products.models import Order
from app.users.models import TelegramUser as User

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
