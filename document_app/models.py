from django.db import models

from user_app.models import CustomUser
from project_app.models import Projects


class Documents(models.Model):

    ROLE_IN_SYSTEM_CHOICES = [
        ('1', 'Без статуса'),
        ('2', 'Черновик'),
        ('3', 'На согласовании'),
        ('4', 'Действующий'),
        ('5', 'Завершённый'),
        ('6', 'Расторгнутый'),
        ('7', 'Аннулированный')
    ]
    TYPE_CHOICES = [
        ('01', 'Договор'),
        ('02', 'Регистрация объекта в государственном реестре'),
        ('03', 'Правоустанавливающие документы'),
        ('04', 'Проектные документы'),
        ('05', 'Экспертиза'),
        ('06', 'Страхование'),
        ('07', 'Разрешительные документы и акты ввода в эксплуатацию'),
        ('08', 'Исполнительно-техническая документация по строительству'),
        ('09', 'Эксплуатационные документы'),
        ('10', 'Обучение персонала'),
        ('11', 'Документы сезонные в эксплуатационный период'),
        ('12', 'Нормативно-правовые акты'),
        ('13', 'Иные документы')
    ]

    name = models.CharField(max_length=255, verbose_name='Наименование документа')
    status = models.CharField(max_length=4,
                              choices=ROLE_IN_SYSTEM_CHOICES,
                              default='CU',
                              verbose_name='Статус')
    doc_type = models.CharField(max_length=100,
                                choices=TYPE_CHOICES,
                                default='01',
                                verbose_name='Тип')
    duration = models.DateField(verbose_name='Срок действия')
    doc = models.FileField(upload_to='uploads_documents/', verbose_name='Документ', null=True, blank=True)

    users = models.ManyToManyField(
        CustomUser,
        related_name="document_to_user",
        blank=True,
    )

    projects = models.ManyToManyField(
        Projects,
        related_name="document_to_project",
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Документы"
        verbose_name_plural = "Документы"
