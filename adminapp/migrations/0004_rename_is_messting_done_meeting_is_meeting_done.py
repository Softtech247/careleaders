# Generated by Django 5.0.6 on 2024-05-16 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_rename_is_done_meeting_is_messting_done'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='is_messting_done',
            new_name='is_meeting_done',
        ),
    ]