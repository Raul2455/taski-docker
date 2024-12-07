"""
Модуль, содержащий модели для приложения API.

Определяет структуру данных и поведение модели Task.
"""

from django.db import models


class Task(models.Model):
    """
    Модель задачи, представляющая элемент списка дел.

    Атрибуты:
        title (CharField): Заголовок задачи.
        description (TextField): Описание задачи.
        completed (BooleanField): Статус выполнения задачи.
    """

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        """
        Возвращает строковое представление модели Task.

        Returns:
            str: Заголовок задачи.
        """
        return self.title
