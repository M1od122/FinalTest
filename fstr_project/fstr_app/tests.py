from rest_framework import status
from rest_framework.test import APITestCase
from .models import Pass

# Создание тестов для API
class PassAPITestCase(APITestCase):

    def setUp(self):
        # Создаем объект перевала для тестирования
        self.Pass_data = {
            'name': 'Test Pass',
            'coordinates': '45.0, 30.0',
            'height': 1000,
            'user_name': 'John Doe',
            'user_email': 'john.doe@example.com',
            'user_phone': '1234567890',
            'photos': ['http://example.com/photo1.jpg'],
        }

    def test_submit_data(self):
        # Тестируем метод submitData
        response = self.client.post('/submitData/', self.Pass_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('id', response.data)

    def test_get_pass(self):
        # Сначала создаем перевал
        response = self.client.post('/submitData/', self.Pass_data, format='json')
        pass_id = response.data['id']

        # Теперь получаем созданный перевал
        response = self.client.get(f'/submitData/{pass_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.Pass_data['name'])

    def test_edit_pass(self):
        # Сначала создаем перевал
        response = self.client.post('/submitData/', self.Pass_data, format='json')
        pass_id = response.data['id']

        # Теперь редактируем перевал
        updated_data = {
            'name': 'Updated Test Pass'
        }
        response = self.client.patch(f'/submitData/edit/{pass_id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['state'], 1)

        # Проверяем, что данные обновились
        response = self.client.get(f'/submitData/{pass_id}/')
        self.assertEqual(response.data['name'], 'Updated Test Pass')

    def test_get_user_passes(self):
        self.client.post('/submitData/', self.Pass_data, format='json')
        response = self.client.get('/submitData/?user__email=john.doe@example.com')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)  # Убедимся, что есть перевалы по данному email

# Создание теста для методов класса
class PassModelTest(TestCase):
    def setUp(self):
        # Создаем объект перевала для тестирования
        self.pass_obj = Pass.objects.create(
            name='Test Pass',
            coordinates='45.0, 30.0',
            height=1000,
            user_name='John Doe',
            user_email='john.doe@example.com',
            user_phone='1234567890',
            photos=['http://example.com/photo1.jpg'],
            status='new'
        )

    def test_pass_creation(self):
        # Проверка, что объект создался
        self.assertEqual(self.pass_obj.name, 'Test Pass')
        self.assertEqual(self.pass_obj.user_email, 'john.doe@example.com')

    def test_pass_retrieval(self):
        # Проверка получения объекта по id
        pass_obj = Pass.objects.get(id=self.pass_obj.id)
        self.assertEqual(pass_obj.name, self.pass_obj.name)