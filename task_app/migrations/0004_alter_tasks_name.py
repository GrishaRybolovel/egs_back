# Generated by Django 4.2.8 on 2024-01-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_app", "0003_alter_tasks_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasks",
            name="name",
            field=models.CharField(max_length=1023, verbose_name="Задание"),
        ),
    ]