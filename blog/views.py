from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.views import APIView
from .models import *
from .services import BlogService
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .services2 import PostStatisticsService



class PostListView(generics.ListCreateAPIView):
    """
    View для работы со списком записей блога.
    """

    queryset = Post.objects.all()  
    serializer_class = PostSerializer  

    def get(self, request):
        """
        Получает список всех записей блога с пагинацией.

        :param request: HTTP запрос.
        :return: Ответ с записями блога и статусом HTTP.
        """
        posts = self.get_queryset()  

        
        serializer = self.get_serializer(posts, many=True)

        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Создает новую запись в блоге.

        :param request: HTTP запрос.
        :return: Ответ с созданной записью или сообщением об ошибке и статусом HTTP.
        """
        serializer = self.get_serializer(data=request.data) 

        if serializer.is_valid():
            # Если данные валидны, создаем новую запись и возвращаем ее с статусом 201 Created
            post = serializer.save()  # Сохраняем объект, который возвращает сам объект Post
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        else:
            # Если данные не валидны, возвращаем ошибку 400 Bad Request с деталями
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PostDetailView(APIView):
    """
    View для работы с отдельной записью блога.
    """


    def get(self, request, post_id):
        """
        Получает одну запись блога по идентификатору.

        :param request: HTTP запрос.
        :param post_id: Идентификатор записи блога.
        :return: Ответ с записью блога или сообщением об ошибке и статусом HTTP.
        """
        
        post = BlogService.get_post_by_id(post_id)

        if post:
            # Если запись найдена, сериализуем ее и возвращаем с статусом 200 OK
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Если запись не найдена, возвращаем ошибку 404 Not Found
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)



    def put(self, request, post_id):
        """
        Обновляет существующую запись в блоге.

        :param request: HTTP запрос.
        :param post_id: Идентификатор записи блога.
        :return: Ответ с обновленной записью или сообщением об ошибке и статусом HTTP.
        """
        
        post = BlogService.get_post_by_id(post_id)

        if post:
            # Сериализуем данные запроса
            serializer = PostSerializer(post, data=request.data)

            if serializer.is_valid():
                # Если данные валидны, обновляем запись и возвращаем ее с статусом 200 OK
                updated_post = BlogService.update_post(post_id, serializer.validated_data['title'], serializer.validated_data['content'])
                return Response(PostSerializer(updated_post).data, status=status.HTTP_200_OK)
            else:
                # Если данные не валидны, возвращаем ошибку 400 Bad Request с деталями
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Если запись не найдена, возвращаем ошибку 404 Not Found
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, post_id):
        """
        Удаляет запись в блоге.

        :param request: HTTP запрос.
        :param post_id: Идентификатор записи блога.
        :return: Ответ с сообщением о статусе операции.
        """
        # Используем BlogService для удаления записи
        deleted = BlogService.delete_post(post_id)

        if deleted:
            # Если запись была удалена, возвращаем статус 204 No Content
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            # Если запись не найдена, возвращаем ошибку 404 Not Found
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)




class PostSearchView(APIView):
    """
    Представление для поиска записей блога.
    """

    def get_queryset(self):
        queryset = Post.objects.all()
        title = self.request.query_params.get('title', None)
        content = self.request.query_params.get('content', None)

        if title:
            queryset = queryset.filter(title__icontains=title)  # Поиск по названию
        if content:
            queryset = queryset.filter(content__icontains=content)  # Поиск по содержанию
            
        return queryset

    def get(self, request):
        """
        Обрабатывает GET-запрос для поиска записей блога по заголовку или содержимому с пагинацией.
        """
        query = request.GET.get('query', '')  # Получаем строку для поиска из параметров запроса
        page_number = request.GET.get('page', 1)  # Получаем номер страницы
        page_size = request.GET.get('page_size', 10)  # Получаем размер страницы
        
        # Ищем записи с помощью BlogService и передаем параметры для пагинации
        posts = BlogService.search_posts(query, page_number, page_size)
        
        # Сериализуем полученные записи
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)






class PostStatisticsView(APIView):
    """
    Представление для получения статистики постов по пользователю.
    """

    def get(self, request, user_id):
        """
        Получение статистики постов для указанного пользователя.
        """
        try:
            # Получаем посты, принадлежащие пользователю с user_id
            posts = Post.objects.filter(user_id=user_id)
            post_count = posts.count()

            # Получаем среднее количество постов за месяц
            average_posts_per_month = PostStatisticsService.get_average_posts_per_month(user_id)

            # Сбор статистики
            statistics = {
                'user_id': user_id,
                'post_count': post_count,
                'average_posts_per_month': average_posts_per_month,
                # Дополнительные метрики можно добавить здесь
            }

            return Response(statistics, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




