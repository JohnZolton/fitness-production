# Generated by Django 4.1.4 on 2023-01-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracking", "0004_alter_metrics_edited"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="yesterday_synced",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
