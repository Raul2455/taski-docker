"""
Модуль, содержащий сериализаторы для приложения API.

Определяет сериализацию и десериализацию данных модели Task.
"""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Task.

    Определяет, какие поля модели Task будут включены в сериализацию.
    """

    class Meta:
        """
        Метаданные для сериализатора TaskSerializer.

        Указывает модель и поля, которые должны быть сериализованы.
        """

        model = Task
        fields = ('id', 'title', 'description', 'completed')
