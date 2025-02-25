from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pass
from .serializers import PassSerializer

@api_view(['POST'])
def submit_data(request):
    if request.method == 'POST':
        serializer = PassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Сохраняем данные в БД
            return Response({
                'status': 200,
                'message': 'Отправлено успешно',
                'id': serializer.instance.id  # Возвращаем ID новой записи
            })
        return Response({
            'status': 400,
            'message': 'Bad Request'
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_pass(request, id):
    try:
        pass_obj = Pass.objects.get(id=id)  # Получаем объект по ID
        serializer = PassSerializer(pass_obj)
        return Response(serializer.data)
    except Pass.DoesNotExist:
        return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def edit_pass(request, id):
    try:
        pass_obj = Pass.objects.get(id=id, status='new')  # Проверяем статус
        serializer = PassSerializer(pass_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Сохраняем изменения
            return Response({'state': 1, 'message': 'Запись успешно обновлена'})
        return Response({'state': 0, 'message': 'Ошибка валидации'}, status=status.HTTP_400_BAD_REQUEST)
    except Pass.DoesNotExist:
        return Response({'state': 0, 'message': 'Запись не найдена или не может быть отредактирована'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_user_passes(request):
    email = request.query_params.get('user__email')  # Получаем email из параметров запроса
    if email:
        passes = Pass.objects.filter(user_email=email)  # Фильтруем по email
        serializer = PassSerializer(passes, many=True)
        return Response(serializer.data)
    return Response({'message': 'Email не предоставлен'}, status=status.HTTP_400_BAD_REQUEST)
