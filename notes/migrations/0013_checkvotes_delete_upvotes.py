# Generated by Django 4.1.2 on 2022-11-16 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notes", "0012_alter_notes_user_alter_signup_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Checkvotes",
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
                ("action", models.CharField(max_length=10)),
                (
                    "likedNote",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="notes.notes"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="Upvotes",),
    ]