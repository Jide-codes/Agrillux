# Generated by Django 4.1.3 on 2022-11-23 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0023_customerfeedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerfeedback',
            old_name='Email',
            new_name='email',
        ),
    ]
