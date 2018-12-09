from oscar.apps.address.abstract_models import AbstractBillingAddress
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class BillingAddress(AbstractBillingAddress):
    phone_number = PhoneNumberField(
        _("Phone number"), blank=True,
        help_text=_("In case we need to call you about your order"))


from oscar.apps.order.models import *  # noqa isort:skip
