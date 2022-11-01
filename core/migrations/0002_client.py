# Generated by Django 4.1.2 on 2022-10-24 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("last_name", models.CharField(max_length=100, verbose_name="Name")),
                ("email", models.EmailField(max_length=100, verbose_name="E-mail")),
            ],
        ),
    ]
