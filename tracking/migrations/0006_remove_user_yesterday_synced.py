# Generated by Django 4.1.4 on 2023-01-19 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tracking", "0005_user_yesterday_synced"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="yesterday_synced",
        ),
    ]
