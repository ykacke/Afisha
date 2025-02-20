from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def authorization_api_view(request):
    username = request.data.get['username']
    password = request.data.get['password']

    user = authenticate(username=username, password=password)

    if user:
        token = Token.objects.get(user=user)
        return Response({'token': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'error': 'Username credentiels are wrohg!'})


@api_view(['POST'])
def registraton_api_view(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = User.objects.create_user(username=username, password= password)

    return Response(status=status.HTTP_201_CREATED, data={'user_id': user.id})