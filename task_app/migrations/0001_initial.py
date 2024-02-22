# Generated by Django 4.2.8 on 2024-01-09 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (
            "project_app",
            "0003_alter_projects_cost_alter_projects_date_creation_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tasks",
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
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=1023, verbose_name="Задание"
                    ),
                ),
                ("created", models.DateField(verbose_name="Дата создания")),
                ("completion", models.DateField(verbose_name="Срок выполнения")),
                (
                    "done",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата выполнения"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="project_app.projects",
                        verbose_name="Проект",
                    ),
                ),
                (
                    "task_to_user",
                    models.ManyToManyField(
                        blank=True,
                        related_name="task_to_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователи",
                    ),
                ),
            ],
        ),
    ]