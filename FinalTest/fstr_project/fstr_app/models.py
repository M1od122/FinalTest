from django.db import models

class Pass(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=255)  # Название перевала
    coordinates = models.CharField(max_length=100)  # Координаты перевала
    height = models.FloatField()  # Высота перевала
    user_name = models.CharField(max_length=255)  # ФИО пользователя
    user_email = models.EmailField()  # Email пользователя
    user_phone = models.CharField(max_length=20)  # Телефон пользователя
    photos = models.JSONField()  # Список URL-адресов фотографий
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')  # Статус модерации

    def __str__(self):
        return self.name
