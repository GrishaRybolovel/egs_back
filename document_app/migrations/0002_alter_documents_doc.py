# Generated by Django 4.2.8 on 2024-02-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("document_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="documents",
            name="doc",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="uploads_documents/",
                verbose_name="Документ",
            ),
        ),
    ]
