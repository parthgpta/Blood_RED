# Generated by Django 2.0.13 on 2019-07-14 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_profile_about_me'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='bio',
        ),
    ]
