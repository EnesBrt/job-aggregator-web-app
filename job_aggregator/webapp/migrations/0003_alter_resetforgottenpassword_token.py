# Generated by Django 4.2.10 on 2024-02-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0002_resetforgottenpassword"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resetforgottenpassword",
            name="token",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
