# Generated by Django 4.1.3 on 2022-11-15 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_rename_name_customer_fullname_customer_passwoord_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='passwoord',
        ),
    ]