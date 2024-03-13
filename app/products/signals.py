from aiogram.types import LabeledPrice
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync

from app.products.models import Order
from bot.misc import bot

CLICK = "398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065"
PAYME = "371317599:TEST:1710287106018"
CLICK_PHOTO = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgWGCXrpS2g54YYm0eTzAHHFzY7Kj3ZXEcbg&usqp=CAU"
PAYME_PHOTO = "https://synthesis.uz/wp-content/uploads/2022/01/payme-1920x1080-1.jpg"


@receiver(post_save, sender=Order)
def send_new_user_notification(sender, instance, created, **kwargs):
    if created:
        sync_send_invoice = async_to_sync(bot.send_invoice)
        price = LabeledPrice(label="Payme orqali to'lov", amount=100000)
        invoice_data = {
            "chat_id": instance.user_id,
            "photo_url": CLICK_PHOTO if instance.cash_type == Order.CashTYPE.CLICK else PAYME_PHOTO,
            "currency": "uzs",
            "title": "Anjan",
            "description": "Muzqaymoqlar haridi",
            "payload": str(instance.pk),
            "provider_token": CLICK if instance.cash_type == Order.CashTYPE.CLICK else PAYME,
            "prices": [price]
        }
        sync_send_invoice(**invoice_data)
