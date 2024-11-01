
# GET /api/posts — получить список всех постов
# GET /api/posts/{id} — получить пост по идентификатору
# POST /api/posts — создать новый пост
# PUT /api/posts/{id} — обновить пост по идентификатору
# DELETE /api/posts/{id} — удалить пост по идентификатору
# GET /api/posts/search — искать посты по названию или содержанию
# GET /api/posts/statistics/{user_id} — получить статистику постов по пользователю


# GET /api/posts

# GET /api/posts/5/

# GET /api/posts

# PUT /api/posts

# DELETE /api/posts/3/



# api/posts/search/?page_size=3

# GET /api/posts/search — искать посты по названию или содержанию
http://0.0.0.0:8001/api/posts/search/?1&page_size=10

GET /api/posts/search?content=текст
GET /api/posts/search?title=пример
http://0.0.0.0:8001/api/posts/search/?title=%D0%A1%D0%B5%D0%B4%D1%8C%D0%BC%D0%B0%D1%8F
[
    {
        "id": 1,
        "title": "Пример поста 1",
        "content": "Это содержимое первого поста.",
        "created_at": "2024-01-01T12:00:00Z",
        "updated_at": "2024-01-01T12:00:00Z"
    },
    {
        "id": 2,
        "title": "Пример поста 2",
        "content": "Это содержимое второго поста.",
        "created_at": "2024-01-02T12:00:00Z",
        "updated_at": "2024-01-02T12:00:00Z"
    }
]





# GET /api/posts/statistics/{user_id} 
# GET /api/posts/statistics/1/
# GET /api/posts/statistics/4/






# mkdir API

# cd API

# python3 -m venv venv
# . venv/bin/activate

# git clone https://github.com/takhmina1/API.git





sudo apt update
sudo apt install -y docker.io




sudo usermod -aG docker $USER



sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose



docker --version
docker-compose --version

# git clone https://github.com/takhmina1/API.git
cd blog_api


Вход в консоль PostgreSQL (введите свой пароль при необходимости)
# sudo -u postgres psql

Создание новой базы данных
# CREATE DATABASE blog_db;

Создание пользователя с паролем (замените "password" на ваш пароль)
# CREATE USER blog_user WITH PASSWORD 'password';

 Предоставление прав пользователю на базу данных
# GRANT ALL PRIVILEGES ON DATABASE blog_db TO blog_user;

 Выход из PostgreSQL
# \q

docker-compose up --build


docker-compose exec web python manage.py migrate


docker-compose exec web python manage.py createsuperuser



# docker-compose up --build







