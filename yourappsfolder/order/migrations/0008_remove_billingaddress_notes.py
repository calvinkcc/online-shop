# Generated by Django 2.0.9 on 2018-11-26 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20181125_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='notes',
        ),
    ]
