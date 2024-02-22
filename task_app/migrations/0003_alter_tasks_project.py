# Generated by Django 4.2.8 on 2024-01-11 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "project_app",
            "0003_alter_projects_cost_alter_projects_date_creation_and_more",
        ),
        ("task_app", "0002_alter_tasks_completion_alter_tasks_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasks",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="project_app.projects",
                verbose_name="Проект",
            ),
        ),
    ]