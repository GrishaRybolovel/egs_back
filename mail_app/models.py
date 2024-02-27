from django.db import models
from user_app.models import CustomUser
from message_app.models import Messages
from project_app.models import Projects


class Mails(models.Model):
    name = models.CharField(max_length=1023, verbose_name='Описание')
    naming = models.CharField(max_length=1023, verbose_name='Наименование отправителя/получателя', blank=True, null=True)
    created = models.DateField(verbose_name='Дата создания', auto_now=True, blank=True, null=True)
    date_reg = models.DateField(verbose_name='Дата регистрации', null=True, blank=True)
    number = models.CharField(max_length=1023, verbose_name='Номер', null=True, blank=True)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.deletion.CASCADE,
        verbose_name='Автор'
    )
    completion = models.DateField(verbose_name='Срок выполнения', null=True, blank=True)
    done = models.DateField(verbose_name='Дата выполнения', null=True, blank=True)
    type = models.CharField(max_length=256, verbose_name='Тип', blank=True, null=True)
    doc = models.FileField(upload_to='media/', verbose_name='Документ', null=True, blank=True)
    projects_to_mails = models.ForeignKey(
        Projects,
        on_delete=models.deletion.CASCADE,
        related_name="projects_to_mails",
        null=True,
        blank=True,
        verbose_name="Объект"
    )

    mail_to_user = models.ManyToManyField(
        CustomUser,
        related_name="mail_to_user",
        blank=True,
        verbose_name="Пользователи"
    )

    mail_to_message = models.ManyToManyField(
        Messages,
        related_name="mail_to_message",
        blank=True,
        verbose_name="Сообщения"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Письма'
        verbose_name_plural = 'Письма'
