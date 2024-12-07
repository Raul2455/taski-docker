"""
Модуль для конфигурации приложения API в Django.

Определяет настройки и параметры для приложения API.
"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Класс конфигурации для приложения API.

    Устанавливает параметры по умолчанию для приложения, такие как тип поля
    для автоинкрементных ключей и имя приложения.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
