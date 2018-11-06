from oscar.apps.checkout.models import *  # noqa isort:skip

from django.db import models


class Contact(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(max_length=50,unique =True)
    phone= models.CharField(max_length=300)
    comment= models.TextField()

    class Meta:
      db_table = "contact_info"

    def __str__(self):
         return self.name