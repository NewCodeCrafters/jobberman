from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


class User(AbstractUser):
    first_name = models.CharField(max_length=13)
    last_name = models.CharField(max_length=13)
    phone_number = models.CharField(
        max_length=12,
        verbose_name=_("Phone Number"),
        unique=True,
        validators=[MinLengthValidator(11)],
    )
    username = models.CharField(
        _("username"),
        max_length=150,
        blank=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    
    
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "username", "last_name", "phone_number"]
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    
class Meta:
    verbose_name = "User"
    verbose_name_plural = "Users"

    
