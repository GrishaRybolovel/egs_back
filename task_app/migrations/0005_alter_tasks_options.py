# Generated by Django 4.2.8 on 2024-02-16 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("task_app", "0004_alter_tasks_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tasks",
            options={"verbose_name": "Задачи", "verbose_name_plural": "Задачи"},
        ),
    ]
