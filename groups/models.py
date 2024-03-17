from django.db import models
from document_app.models import Documents
from mail_app.models import Mails
from project_app.models import Projects
from task_app.models import Tasks
from user_app.models import CustomUser


# Create your models here.

class DepartmentGroup(models.Model):
    name = models.CharField(max_length=100)
    parent_group = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    children_group = models.ManyToManyField(
        'self',
        related_name='dep_to_children',
        blank=True,
        verbose_name='Дети'
    )

    heads = models.ManyToManyField(
        CustomUser,
        related_name='dep_head_to_user',
        blank=True,
        verbose_name='Глава отдела'
    )

    participants = models.ManyToManyField(
        CustomUser,
        related_name='dep_part_to_user',
        blank=True,
        verbose_name='Участник отдела'
    )

    documents = models.ManyToManyField(
        Documents,
        related_name='doc_to_user',
        blank=True,
        verbose_name='Документы'
    )

    mails = models.ManyToManyField(
        Mails,
        related_name='mail_to_user',
        blank=True,
        verbose_name='Письма'
    )

    projects = models.ManyToManyField(
        Projects,
        related_name='project_to_user',
        blank=True,
        verbose_name='Объекты'
    )

    tasks = models.ManyToManyField(
        Tasks,
        related_name='task_to_user',
        blank=True,
        verbose_name='Задачи'
    )

    def __str__(self):
        return self.name