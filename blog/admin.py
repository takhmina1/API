from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    """
    Админский интерфейс для управления записями блога.
    Настройка отображения и фильтрации записей в админ-панели.
    """
    list_display = ('id', 'title', 'created_at', 'updated_at')  
    list_filter = ('created_at',)  # Фильтрация по дате создания
    search_fields = ('title', 'content')  # Поиск по заголовку и содержимому
    ordering = ('-created_at',)  # Сортировка по дате создания в порядке убывания

admin.site.register(Post, PostAdmin)
