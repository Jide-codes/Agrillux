# Generated by Django 4.1.3 on 2022-11-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0022_remove_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerFeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('Email', models.EmailField(blank=True, max_length=200, null=True)),
                ('comment', models.TextField(blank=True, max_length=100000, null=True)),
            ],
        ),
    ]
