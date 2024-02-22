from django.db import models
from user_app.models import CustomUser
from project_app.models import Projects


class Tasks(models.Model):
    name = models.CharField(max_length=1023, verbose_name='Задание')
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.deletion.CASCADE,
        verbose_name='Автор'
    )
    created = models.DateField(verbose_name='Дата создания', auto_now=True)
    completion = models.DateField(verbose_name='Срок выполнения', null=True, blank=True)
    done = models.DateTimeField(verbose_name='Дата выполнения', null=True, blank=True)
    project = models.ForeignKey(
        Projects,
        on_delete=models.deletion.CASCADE,
        related_name="tasks",
        null=True,
        blank=True,
        verbose_name='Проект'
    )
    task_to_user = models.ManyToManyField(
        CustomUser,
        related_name="task_to_user",
        blank=True,
        verbose_name="Пользователи"
    )

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'
