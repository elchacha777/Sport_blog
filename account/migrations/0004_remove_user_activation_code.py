# Generated by Django 3.1 on 2021-03-11 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210311_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='activation_code',
        ),
    ]
