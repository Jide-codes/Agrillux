# Generated by Django 4.1.3 on 2022-11-18 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0017_alter_order_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='User',
            new_name='user',
        ),
    ]
