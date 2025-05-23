# Generated by Django 4.1.9 on 2023-05-07 16:06

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gqlauth", "0003_delete_captcha"),
    ]

    operations = [
        migrations.CreateModel(
            name="Captcha",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("text", models.CharField(editable=False, max_length=50)),
                ("insert_time", models.DateTimeField(auto_now_add=True)),
                ("tries", models.IntegerField(default=0)),
                (
                    "image",
                    models.ImageField(
                        editable=False,
                        help_text="url for the captcha image",
                        upload_to="captcha/%Y/%m/%d/",
                    ),
                ),
            ],
        ),
    ]
