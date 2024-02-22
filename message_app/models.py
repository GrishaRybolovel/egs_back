from django.db import models
from user_app.models import CustomUser
from task_app.models import Tasks


class Messages(models.Model):
    message = models.TextField(max_length=1024, verbose_name='Сообщение', blank=True, null=True)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.deletion.CASCADE
    )
    task = models.ForeignKey(
        Tasks,
        on_delete=models.deletion.CASCADE
    )
    created = models.DateField(auto_now=True, blank=True, null=True)
    doc = models.FileField(upload_to='messages_docs', blank=True, null=True)

    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'
