# Generated by Django 4.1.6 on 2023-08-28 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0005_rename_summary_book_description_remove_book_author_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Genre",
        ),
    ]
