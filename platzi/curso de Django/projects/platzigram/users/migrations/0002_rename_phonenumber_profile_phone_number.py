# Generated by Django 4.0 on 2022-01-10 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phonenumber',
            new_name='phone_number',
        ),
    ]
