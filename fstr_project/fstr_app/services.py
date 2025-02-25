from .models import Pass


class PassService:
    # Метод для добавления нового перевала
    @staticmethod
    def add_pass(data):
        try:
            # Создаем новый объект Pass и сохраняем его в базе данных
            new_pass = Pass(
                coordinates=data['coordinates'],
                height=data['height'],
                name=data['name'],
                user_name=data['user_name'],
                user_email=data['user_email'],
                user_phone=data['user_phone'],
                images=data['images']
            )
            new_pass.save()  # Сохраняем запись в базе данных
            return {"status": 200, "message": "Отправлено успешно", "id": new_pass.id}
        except Exception as e:
            # Если произошла ошибка, возвращаем сообщение об ошибке
            return {"status": 500, "message": str(e)}

    # Метод для получения перевала по ID
    @staticmethod
    def get_pass_by_id(pass_id):
        try:
            pass_obj = Pass.objects.get(id=pass_id)  # Ищем объект по ID
            return {"status": 200, "message": "Успех", "data": pass_obj}
        except Pass.DoesNotExist:
            return {"status": 404, "message": "Перевал не найден"}

    # Метод для обновления перевала
    @staticmethod
    def update_pass(pass_id, data):
        try:
            # Получаем перевал, который еще не прошел модерацию (status='new')
            pass_obj = Pass.objects.get(id=pass_id, status='new')

            # Обновляем поля перевала, если они были переданы
            pass_obj.name = data.get('name', pass_obj.name)
            pass_obj.coordinates = data.get('coordinates', pass_obj.coordinates)
            pass_obj.height = data.get('height', pass_obj.height)
            pass_obj.user_name = data.get('user_name', pass_obj.user_name)
            pass_obj.user_email = data.get('user_email', pass_obj.user_email)
            pass_obj.user_phone = data.get('user_phone', pass_obj.user_phone)
            pass_obj.images = data.get('images', pass_obj.images)

            pass_obj.save()  # Сохраняем обновленную запись в базе
            return {"state": 1, "message": "Успешно отредактировано"}
        except Pass.DoesNotExist:
            # Если запись не найдена или в процессе модерации, возвращаем ошибку
            return {"state": 0, "message": "Запись не найдена или в процессе модерации"}
