# Generated by Django 4.1.3 on 2022-11-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='Order',
            new_name='order',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='mobile',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
