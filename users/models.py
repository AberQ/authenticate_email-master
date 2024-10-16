from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']




class State(models.Model):
    title = models.CharField(max_length=255)  # Заголовок статьи
    content = models.TextField()  # Основной текст статьи
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания статьи
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор статьи

    def __str__(self):
        return self.title