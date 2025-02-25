from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import PassService
from .serializers import PassSerializer

class SubmitDataView(APIView):
    def post(self, request):
        # Получаем данные из тела запроса
        data = request.data
        result = PassService.add_pass(data)  # Добавляем новый перевал в базу
        return Response(result, status=result["status"])

class GetPassView(APIView):
    def get(self, request, id):
        # Получаем перевал по ID
        result = PassService.get_pass_by_id(id)
        return Response(result, status=result["status"])

class UpdatePassView(APIView):
    def patch(self, request, id):
        # Получаем данные для обновления
        data = request.data
        result = PassService.update_pass(id, data)  # Обновляем перевал по ID
        return Response(result, status=status.HTTP_200_OK)


