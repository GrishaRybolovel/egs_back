# Generated by Django 4.2.8 on 2024-02-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_app", "0005_alter_tasks_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="tasks",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание задачи"
            ),
        ),
        migrations.AddField(
            model_name="tasks",
            name="doc",
            field=models.FileField(blank=True, null=True, upload_to="media"),
        ),
    ]
