# Generated by Django 4.2.8 on 2024-02-16 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("message_app", "0002_alter_messages_task"),
        ("project_app", "0004_alter_projects_date_creation_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Mails",
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
                ("name", models.CharField(max_length=1023, verbose_name="Описание")),
                (
                    "naming",
                    models.CharField(
                        max_length=1023,
                        verbose_name="Наименование отправителя/получателя",
                    ),
                ),
                (
                    "created",
                    models.DateField(auto_now=True, verbose_name="Дата создания"),
                ),
                ("date_reg", models.DateField(verbose_name="Дата регистрации")),
                ("number", models.CharField(max_length=1023, verbose_name="Номер")),
                (
                    "completion",
                    models.DateField(
                        blank=True, null=True, verbose_name="Срок выполнения"
                    ),
                ),
                (
                    "done",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата выполнения"
                    ),
                ),
                ("type", models.CharField(max_length=256, verbose_name="Тип")),
                (
                    "doc",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="uploads_mails/",
                        verbose_name="Документ",
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
                    "mail_to_message",
                    models.ManyToManyField(
                        blank=True,
                        related_name="mail_to_message",
                        to="message_app.messages",
                        verbose_name="Сообщения",
                    ),
                ),
                (
                    "mail_to_user",
                    models.ManyToManyField(
                        blank=True,
                        related_name="mail_to_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователи",
                    ),
                ),
                (
                    "projects_to_mails",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects_to_mails",
                        to="project_app.projects",
                        verbose_name="Объект",
                    ),
                ),
            ],
            options={
                "verbose_name": "Письма",
                "verbose_name_plural": "Письма",
            },
        ),
    ]