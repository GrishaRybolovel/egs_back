from django.db import models
from user_app.models import CustomUser
from project_app.models import Projects
import datetime


class Tasks(models.Model):
    name = models.CharField(max_length=1023, verbose_name='Задание')
    description = models.TextField(verbose_name='Описание задачи', null=True, blank=True)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.deletion.CASCADE,
        verbose_name='Автор'
    )
    created = models.DateField(verbose_name='Дата создания', auto_now=True)
    completion = models.DateField(verbose_name='Срок выполнения', null=True, blank=True)
    done = models.DateTimeField(verbose_name='Дата выполнения', null=True, blank=True)
    doc = models.FileField(upload_to='media', blank=True, null=True)
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

    @classmethod
    def get_tasks_for_current_month(cls, user_id):

        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month

        first_day_of_month = datetime.datetime(current_year, current_month, 1).date()
        last_day_of_month = (first_day_of_month + datetime.timedelta(days=32)).replace(day=1) - datetime.timedelta(days=1)

        try:
            tasks = cls.objects.filter(
                task_to_user=CustomUser.objects.get(id=user_id),
                created__lte=last_day_of_month,
                completion__gte=first_day_of_month
            )
        except Exception as e:
            return {}

        tasks_by_day = {}
        for task in tasks:
            current_date = max(task.created, first_day_of_month)
            while current_date <= min(task.completion, last_day_of_month):
                tasks_by_day.setdefault(str(current_date), []).append(task)
                current_date += datetime.timedelta(days=1)

        return tasks_by_day

    @property
    def type(self):
        if self.project:
            return self.project.proj_type if hasattr(self.project, 'proj_type') else None
        else:
            return None

