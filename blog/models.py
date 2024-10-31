from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Модель для представления записи блога.
    Каждая запись содержит уникальный идентификатор, заголовок, содержимое,
    а также временные метки для отслеживания даты создания и последнего обновления.
    """
    

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  

    # Заголовок записи, ограничен 255 символами
    title = models.CharField(max_length=255, verbose_name="Заголовок")

    # Содержимое записи
    content = models.TextField(verbose_name="Содержание")

    # Дата и время создания записи, задается автоматически при первом создании
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    # Дата и время последнего обновления записи, обновляется автоматически при каждом сохранении
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        Удобно для отображения заголовка при выводе объекта, например, в админке.
        """
        return self.title

    class Meta:
        """
        Метаданные модели:
        - Задаем порядок сортировки записей по дате создания (от новых к старым).
        """
        ordering = ['-created_at']
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"
