# Generated by Django 3.1 on 2023-08-21 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('box_app', '0002_auto_20230821_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='username1',
            new_name='username',
        ),
    ]
