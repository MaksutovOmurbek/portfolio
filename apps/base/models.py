from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 255, verbose_name = "ФИО")
    info = models.TextField(verbose_name = 'Инфо о себе')
    desc = models.TextField(verbose_name = 'работа')
    photo = models.ImageField(verbose_name='Фото')


def __str__(self) -> str:
        return f"{self.name} "

class Meta:
    verbose_name = 'Пользовательская'
    verbose_name_plural = 'Пользовательская'