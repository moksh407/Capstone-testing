# Generated by Django 2.0 on 2018-11-23 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0012_remove_userprofile_user_badge_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_badge_text',
        ),
    ]