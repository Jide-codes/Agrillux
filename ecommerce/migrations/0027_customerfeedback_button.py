# Generated by Django 4.1.3 on 2022-11-30 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0026_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerfeedback',
            name='button',
            field=models.BooleanField(default=False),
        ),
    ]
