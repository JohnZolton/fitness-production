# Generated by Django 4.1.4 on 2023-01-17 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracking", "0003_metrics_edited"),
    ]

    operations = [
        migrations.AlterField(
            model_name="metrics",
            name="edited",
            field=models.BooleanField(null=True),
        ),
    ]
