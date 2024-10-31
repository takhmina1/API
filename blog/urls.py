from django.urls import path
from .views import PostListView, PostSearchView, PostDetailView
from .views import PostStatisticsView



urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),  # URL для получения списка записей и создания новой записи
    # path('posts2/search/', PostViewSet.as_view(), name='post-search2'),  # Новый URL для получения списка записей с пагинацией (второй вариант)
    path('posts/search/', PostSearchView.as_view(), name='post-search'),  # URL для поиска записей по заголовку или содержимому
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),  # URL для получения, обновления и удаления записи по идентификатору

    path('posts/statistics/<int:user_id>/', PostStatisticsView.as_view(), name='post-statistics'),
    # path('api/posts/', PostListView3.as_view(), name='post-list'),
]
    





'''

#     path('posts/', PostListView.as_view(), name='post-list'),         # URL для получения списка записей и создания новой записи
#     path('posts/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),  # URL для получения, обновления и удаления записи по идентификатору




GET /posts: маршрут path('posts/', PostListView.as_view(), name='post-list') обрабатывает запросы на получение списка всех сообщений блога и создание новых записей.
GET /posts/{id}: маршрут path('posts/<int:post_id>/', PostDetailView.as_view(), name='post-detail') обрабатывает запросы на получение одной записи блога по идентификатору.
POST /posts: маршрут по тому же URL (posts/) обрабатывает запросы на создание новой записи.
PUT /posts/{id}: этот маршрут обрабатывается в PostDetailView, который обновляет существующую запись.
DELETE /posts/{id}: также обрабатывается в PostDetailView, который удаляет запись блога.

'''




