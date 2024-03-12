from aiogram.types import LabeledPrice
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync

from app.products.models import Order
from bot.misc import bot


@receiver(post_save, sender=Order)
def send_new_user_notification(sender, instance, created, **kwargs):
    if created:
        async_to_sync(bot.send_message)(instance.user.id, "Hello")
        # sync_send_invoice = async_to_sync(bot.send_invoice)
        # sync_send_invoice(instance.user.id, "Qale", "yaxmale", "tttt", "ttetete", "UZS",
        #                   [LabeledPrice(label="ggg", amount=10000)])
