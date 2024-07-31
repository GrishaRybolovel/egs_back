# Generated by Django 4.2.8 on 2024-05-07 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("document_app", "0003_alter_documents_doc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="documents",
            name="status",
            field=models.CharField(
                choices=[
                    ("1", "Без статуса"),
                    ("2", "Черновик"),
                    ("3", "На согласовании"),
                    ("4", "Действующий"),
                    ("5", "Завершённый"),
                    ("6", "Расторгнутый"),
                    ("7", "Аннулированный"),
                ],
                default="1",
                max_length=4,
                verbose_name="Статус",
            ),
        ),
    ]