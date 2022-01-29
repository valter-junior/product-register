from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserRegisterSerializer, UserLoginSerializer

class UserRegistration(CreateAPIView):

    serializer_class = UserRegisterSerializer
    permission_class = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'status code' : status_code,
            'message': 'User registered  successfully',
        }

        return Response(response, status=status_code)


class UserLogin(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'token' : serializer.data['token']
        }

        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

