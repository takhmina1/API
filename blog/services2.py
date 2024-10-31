from django.db.models import Count
from django.db.models.functions import TruncMonth
from .models import Post


class PostStatisticsService:
    """
    Класс для работы со статистикой постов блога.
    """

    @staticmethod
    def get_average_posts_per_month(user_id):
        """
        Возвращает среднее количество постов за месяц у конкретного пользователя.

        :param user_id: Идентификатор пользователя, для которого нужно получить статистику.
        :return: Среднее количество постов за месяц, или 0, если постов нет.
        """
        
        monthly_posts = (
            Post.objects
            .filter(user_id=user_id)  # Фильтруем по user_id
            .annotate(month=TruncMonth('created_at'))  # Группируем по месяцам
            .values('month')  # Получаем только месяц
            .annotate(post_count=Count('id'))  # Считаем количество постов за месяц
            .order_by('month')  # Упорядочиваем по месяцу
        )

        
        if not monthly_posts.exists():
            return 0

        
        total_posts = sum(month['post_count'] for month in monthly_posts)

       
        month_count = monthly_posts.count()

        
        average_posts = total_posts / month_count

        return average_posts
