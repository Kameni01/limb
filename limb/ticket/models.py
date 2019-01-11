from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
    """Category tickets"""
    title = models.CharField("Категория", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

class Ticket(models.Model):
    """Tickets class"""
    user = models.ForeignKey(User, verbose_name="Пользователь",
                            on_delete=models.CASCADE)
    category = models.ForeignKey(Category, "Категория",
                            on_delete=models.CASCADE)
    title = models.Charfield("Тема", max_length=100)
    text = models.TextField("Текст письма", max_length=1000)

    class Meta:
        verbose_name = "Тикет"
        verbose_name_plural = "Тикеты"

    def __str__(self):
        return "{} {}".format(self.title, self.user)
