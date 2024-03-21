from django.db import models
from user_app.models import CustomUser

class Projects(models.Model):
    STATUS_CHOICES = [
        ('1', 'В работе'),
        ('2', 'ПНР'),
        ('3', 'Сезон откл.'),
        ('4', 'СМР'),
        ('5', 'Аварийное откл.')
    ]
    SEASONING_CHOICES = [
        ('1', 'Сезонная'),
        ('2', 'Круглогодичная')
    ]
    TYPE_CHOICES = [
        ('1', 'Эксплуатация'),
        ('2', 'Техническое обслуживание'),
        ('3', 'СМР'),
        ('4', 'Производство')
    ]
    proj_type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default='1',
        verbose_name='Статус объекта'
    )

    name = models.CharField(max_length=255, verbose_name='Название')
    reg_num = models.CharField(max_length=255, verbose_name='Регистрационный № ОПО')
    contract = models.CharField(max_length=255, blank=True, verbose_name='Договор')
    date_creation = models.DateField(verbose_name='Дата договора', auto_now=True, blank=True, null=True)
    date_notification = models.DateField(verbose_name='Дата(для оповещения)', auto_now=True, blank=True, null=True)
    object_type = models.CharField(max_length=255, blank=True, verbose_name='Тип объекта')
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес')
    contact = models.CharField(max_length=255, blank=True, verbose_name='Контактный человек')
    phone = models.CharField(max_length=255, blank=True, verbose_name='Контактный телефон')
    email = models.CharField(max_length=255, blank=True, verbose_name='Контактный e-mail')
    status = models.CharField(
        max_length=4,
        choices=STATUS_CHOICES,
        default='1',
        verbose_name='Статус объекта'
    )
    seasoning = models.CharField(
        max_length=4,
        choices=SEASONING_CHOICES,
        default='1',
        verbose_name='Сезонность'
    )
    cost = models.FloatField(blank=True, null=True, verbose_name='Цена обслуживания', default=0)
    is_archived = models.BooleanField(default=False, blank=True, verbose_name='Архивный')

    project_to_user = models.ManyToManyField(
        CustomUser,
        related_name="project_to_user",
        blank=True,
        verbose_name="Пользователи"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объекты'
        verbose_name_plural = 'Объекты'

class StatusChoiceChange(models.Model):
    TYPE_CHOICES = [
        ('1', 'Статус'),
        ('2', 'Цена'),
    ]

    STATUS_CHOICES = [
        ('1', 'В работе'),
        ('2', 'ПНР'),
        ('3', 'Сезон откл.'),
        ('4', 'СМР'),
        ('5', 'Аварийное откл.')
    ]

    project = models.ForeignKey(
        Projects,
        on_delete=models.deletion.CASCADE
    )

    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default='2',
        verbose_name='Тип'
    )
    value = models.FloatField(null=True, blank=True, verbose_name='Значение')
    status = models.CharField(max_length=255, null=True, blank=True, choices=STATUS_CHOICES)

    date = models.DateField(null=True, blank=True, auto_now=True)
