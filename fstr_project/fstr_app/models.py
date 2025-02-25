from django.db import models

class Pass(models.Model):
    # Координаты перевала
    coordinates = models.CharField(max_length=255)
    # Высота перевала
    height = models.IntegerField()
    # Название перевала
    name = models.CharField(max_length=255)
    # Имя пользователя, который отправил данные
    user_name = models.CharField(max_length=255)
    # Почта пользователя
    user_email = models.EmailField()
    # Телефон пользователя
    user_phone = models.CharField(max_length=15)
    # Список фотографий перевала в формате JSON
    images = models.JSONField()
    # Статус перевала (модерация)
    status = models.CharField(max_length=20, default='new')  # Статус по умолчанию - 'new'

    def __str__(self):
        return f"{self.name} - {self.status}"

