from oscar.apps.checkout.models import *  # noqa isort:skip

from django.db import models


class Contact(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    phone= models.CharField(max_length=300)
    comment= models.TextField()

    class Meta:
      db_table = "contact_info"

    def __str__(self):
         return self.name