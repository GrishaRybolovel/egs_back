from rest_framework import generics, permissions, exceptions, response, views, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import CustomUserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class LoginApi(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        password = request.data["password"]

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        if user.password != password and not user.check_password(password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


class ListUsersView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)
