# Generated by Django 4.2.8 on 2024-01-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasks",
            name="completion",
            field=models.DateField(
                blank=True, null=True, verbose_name="Срок выполнения"
            ),
        ),
        migrations.AlterField(
            model_name="tasks",
            name="created",
            field=models.DateField(auto_now=True, verbose_name="Дата создания"),
        ),
    ]
