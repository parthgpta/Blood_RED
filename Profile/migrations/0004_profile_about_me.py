# Generated by Django 2.0.13 on 2019-07-11 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(default='Hey ,There its me'),
            preserve_default=False,
        ),
    ]
