from .models import Post
from django.db.models import Avg
from .pagination import PostPaginator
from .models import *
from django.core.paginator import Paginator




class BlogService:
    """
    Класс для работы с записями блога.
    """


    @staticmethod
    def get_all_posts(page_number=1, page_size=10):
        """
        Получает все записи блога с пагинацией.

        :param page_number: Номер страницы для пагинации.
        :param page_size: Количество записей на странице.
        :return: Словарь с записями и информацией о пагинации.
        """
        # Получаем все записи блога
        posts = Post.objects.all()  
        # Создаем экземпляр PostPaginator
        paginator = PostPaginator(posts, page_number, page_size)  
        # Возвращаем результат пагинации
        return paginator.paginate() 




    @staticmethod
    def get_post_by_id(post_id):
        """
        Получает одну запись блога по идентификатору.

        :param post_id: Идентификатор записи блога.
        :return: Запись блога или None, если не найдена.
        """
        # Получаем запись по идентификатору
        return Post.objects.filter(id=post_id).first() 




    @staticmethod
    def create_post(title, content):
        """
        Создает новую запись в блоге.

        :param title: Заголовок новой записи.
        :param content: Содержимое новой записи.
        :return: Созданная запись блога.
        """
        # Создаем новую запись
        new_post = Post.objects.create(title=title, content=content)  
        return new_post 




    @staticmethod
    def update_post(post_id, title, content):
        """
        Обновляет существующую запись в блоге.

        :param post_id: Идентификатор записи блога.
        :param title: Новый заголовок записи.
        :param content: Новое содержимое записи.
        :return: Обновленная запись блога или None, если не найдена.
        """
        # Ищем запись по идентификатору
        post = Post.objects.filter(id=post_id).first()  
        if post:
            # Обновляем поля записи
            post.title = title  
            post.content = content  
            post.save()  # Сохраняем изменения
            return post  
        return None  # Если запись не найдена, возвращаем None




    @staticmethod
    def delete_post(post_id):
        """
        Удаляет запись в блоге.

        :param post_id: Идентификатор записи блога.
        :return: True, если запись была удалена, иначе False.
        """
        # Ищем запись по идентификатору
        post = Post.objects.filter(id=post_id).first()  
        if post:
            post.delete()  # Удаляем запись
            return True  
        return False  # Если запись не найдена, возвращаем False




    # @staticmethod
    # def search_posts(query):
    #     """
    #     Ищет записи блога по заголовку или содержимому.

    #     :param query: Строка для поиска.
    #     :return: Записи блога, соответствующие запросу.
    #     """
    #     # Ищем записи, где заголовок или содержимое содержит поисковый запрос
    #     return Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)  






    @staticmethod
    def get_all_posts2(page_number=1, page_size=10):
        """
        Получает все записи блога с пагинацией.

        :param page_number: Номер страницы для пагинации.
        :param page_size: Количество записей на странице.
        :return: Словарь с записями и информацией о пагинации.
        """
        # Получаем все записи блога
        posts = Post.objects.all()  
        # Создаем экземпляр PostPaginator
        paginator = PostPaginator(posts, page_number, page_size)  
        # Возвращаем результат пагинации
        return paginator.paginate()  






    @staticmethod
    def search_posts(query, page_number, page_size):
        """
        Поиск записей блога по заголовку или содержимому.
        Возвращает посты с пагинацией.
        """
        posts = Post.objects.filter(models.Q(title__icontains=query) | models.Q(content__icontains=query))
        paginator = Paginator(posts, page_size)
        page = paginator.get_page(page_number)
        
        return page  # Возвращаем объект страницы, который содержит посты






    @staticmethod
    def get_statistics(user_id):
        """
        Возвращает среднее количество постов за месяц у конкретного юзера.

        :param user_id: Идентификатор пользователя.
        :return: Среднее количество постов за месяц.
        """
        # Предполагаем, что у нас есть связь между Post и User (пользователь, создавший запись)
        return Post.objects.filter(user_id=user_id).annotate(month=ExtractMonth('created_at')).values('month').annotate(avg_posts=Avg('id')).values('avg_posts')
