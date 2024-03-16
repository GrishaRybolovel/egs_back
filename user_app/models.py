from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    # Basic user info
    username = None
    email = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=63, verbose_name='Имя')
    surname = models.CharField(max_length=63, verbose_name='Фамилия')
    last_name = models.CharField(max_length=63, blank=True, null=True, verbose_name='Отчество')

    # Django user info
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    # Custom user info
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='Телефон')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес')
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True)
    date_of_start = models.DateField(verbose_name='Дата начала', blank=True, null=True)
    inn = models.CharField(max_length=256, blank=True, null=True, verbose_name='ИНН')
    snils = models.CharField(max_length=256, blank=True, null=True, verbose_name='СНИЛС')
    passport = models.TextField(max_length=256, blank=True, null=True, verbose_name='Паспорт')
    post = models.CharField(max_length=255, blank=True, null=True, verbose_name='Должность')
    info_about_relocate = models.TextField(max_length=511, blank=True, null=True, verbose_name='Информация о переводе')
    attestation = models.CharField(max_length=255, blank=True, null=True, verbose_name='Аттестация')
    qualification = models.CharField(max_length=255, blank=True, null=True, verbose_name='Повышение квалификации')
    retraining = models.CharField(max_length=255, blank=True, null=True, verbose_name='Проф. подготовка')
    status = models.BooleanField(verbose_name='Статус', default=True)

    is_dark = models.BooleanField(verbose_name='Тема', default=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'