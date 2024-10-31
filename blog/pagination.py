from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PostPaginator:
    """
    Класс для управления пагинацией записей блога.
    """

    def __init__(self, queryset, page_number=1, page_size=10):
        """
        Инициализация класса пагинации.

        :param queryset: Запрос к базе данных для получения записей.
        :param page_number: Номер страницы для пагинации (по умолчанию 1).
        :param page_size: Количество записей на странице (по умолчанию 10).
        """
        self.queryset = queryset  # Сохраняем queryset для дальнейшего использования
        self.page_number = page_number  # Номер страницы
        self.page_size = page_size  # Размер страницы


    def paginate(self):
        """
        Метод для выполнения пагинации.

        :return: Словарь с записями и информацией о пагинации.
        """
        # Создаем объект пагинатора с заданным размером страницы
        paginator = Paginator(self.queryset, self.page_size)  
        
        try:
            # Получаем запрашиваемую страницу
            page = paginator.page(self.page_number)  
        except PageNotAnInteger:
            # Если page_number не является целым числом, возвращаем первую страницу
            page = paginator.page(1)
        except EmptyPage:
            # Если page_number выходит за пределы доступных страниц, возвращаем последнюю страницу
            page = paginator.page(paginator.num_pages)


        # Формируем и возвращаем словарь с записями и информацией о пагинации
        return {
            'posts': page.object_list,  # Записи на текущей странице
            'total_pages': paginator.num_pages,  # Общее количество страниц
            'current_page': page.number,  # Текущая страница
            'has_next': page.has_next(),  # Есть ли следующая страница
            'has_previous': page.has_previous(),  # Есть ли предыдущая страница
            'page_size': self.page_size,  # Размер страницы
            'total_items': paginator.count,  # Общее количество записей
        }

