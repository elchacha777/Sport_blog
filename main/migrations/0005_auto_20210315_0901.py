# Generated by Django 3.1 on 2021-03-15 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='likes',
            new_name='likes_unlikes',
        ),
    ]