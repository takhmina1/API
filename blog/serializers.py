from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField()

    """
    Сериализатор для модели Post.
    Используется для преобразования данных модели в JSON и валидации данных при создании и обновлении записей.
    """

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']

    def validate_title(self, value):
        """
        Валидация заголовка записи.
        Проверяет, что заголовок не пустой и не превышает 255 символов.
        """
        if not value:
            raise serializers.ValidationError("Заголовок не может быть пустым.")
        if len(value) > 255:
            raise serializers.ValidationError("Заголовок не может превышать 255 символов.")
        return value

    def validate_content(self, value):
        """
        Валидация содержимого записи.
        Проверяет, что содержимое не пустое.
        """
        if not value:
            raise serializers.ValidationError("Содержание не может быть пустым.")
        return value
