# Generated by Django 5.0.6 on 2024-05-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_rename_firstname_user_firs_tname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firs_tname',
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
