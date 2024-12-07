"""
Модуль для регистрации модели Task в административной панели Django.

Этот модуль определяет, как модель Task будет отображаться и
управляться в интерфейсе администратора.
"""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """
    Класс для настройки отображения модели Task в административной панели.

    Определяет, какие поля модели Task будут отображаться в списке объектов.
    """

    list_display = ('title', 'description', 'completed')

# Регистрация модели Task с использованием TaskAdmin для управления в админке


admin.site.register(Task, TaskAdmin)
