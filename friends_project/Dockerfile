# Используем официальный образ Python в качестве базового образа
FROM python:3.9-slim-buster

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы requirements.txt из локальной директории внутрь контейнера
COPY requirements.txt .

# Устанавливаем зависимости Python из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы из локальной директории внутрь контейнера
COPY /mysite .

# Выполняем миграции базы данных
RUN python manage.py migrate

# Указываем порт, на котором будет запущен сервер Django
EXPOSE 8000

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
