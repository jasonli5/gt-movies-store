# Generated by Django 5.1.5 on 2025-02-06 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="movie",
        ),
        migrations.RemoveField(
            model_name="review",
            name="user",
        ),
        migrations.DeleteModel(
            name="Movie",
        ),
        migrations.DeleteModel(
            name="Review",
        ),
    ]
