# Generated by Django 4.2.8 on 2024-05-07 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mail_app", "0003_alter_mails_doc"),
    ]

    operations = [
        migrations.AddField(
            model_name="mails",
            name="completion_in",
            field=models.DateField(
                blank=True, null=True, verbose_name="Входящая дата выполнения"
            ),
        ),
        migrations.AddField(
            model_name="mails",
            name="completion_out",
            field=models.DateField(
                blank=True, null=True, verbose_name="Исходящая дата выполнения"
            ),
        ),
        migrations.AddField(
            model_name="mails",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание письма"
            ),
        ),
        migrations.AddField(
            model_name="mails",
            name="func",
            field=models.CharField(
                choices=[("1", "Письмо как задача"), ("2", "Информационное письмо")],
                default="1",
                max_length=4,
                verbose_name="Тип письма",
            ),
        ),
        migrations.AddField(
            model_name="mails",
            name="number_in",
            field=models.CharField(
                blank=True, max_length=127, null=True, verbose_name="Входящий номер"
            ),
        ),
        migrations.AddField(
            model_name="mails",
            name="number_out",
            field=models.CharField(
                blank=True, max_length=127, null=True, verbose_name="Исходящий номер"
            ),
        ),
    ]
