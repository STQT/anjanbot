from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from ckeditor.fields import RichTextField

from imagekit.models import ImageSpecField


class User(AbstractUser):
    """
    Default custom user model for Makro Promo Bot.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class TelegramUser(models.Model):
    id = models.PositiveBigIntegerField(_("Телеграм ID"),
                                        db_index=True,
                                        primary_key=True,
                                        editable=False,
                                        auto_created=False
                                        )
    language = models.CharField(_("Язык пользователя"), max_length=2, blank=True, null=True)
    fullname = models.CharField(_("Имя пользователя"), max_length=100, blank=True, null=True)
    phone = models.CharField(_("Телефонный номер"), max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}, {self.fullname}"

    class Meta:
        verbose_name = _("Телеграм пользователь")
        verbose_name_plural = _("Телеграм пользователи")


class Notification(models.Model):
    class NotificationStatus(models.IntegerChoices):
        CREATED = 0, "Yaratildi"
        SENDED = 1, "Bajarildi"
        PROCEED = 2, "Jarayonda"

    description = RichTextField(max_length=1023, null=True, blank=True)
    status = models.IntegerField(choices=NotificationStatus.choices, default=NotificationStatus.CREATED, editable=False)
    all_chats = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField("Yaratilgan vaqti", auto_now_add=True)

    class Meta:
        verbose_name = "Xabarnoma "
        verbose_name_plural = "Xabarnomalar "


class NotificationShots(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Rasm", upload_to="notification")
    image_compress = ImageSpecField(source='image', format='JPEG',
                                    options={'quality': 60})

    class Meta:
        verbose_name = "Xabarnoma rasmi"
        verbose_name_plural = "Xabarnoma rasmlari "
