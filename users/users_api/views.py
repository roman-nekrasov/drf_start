from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser
from .serializers import SignUpSerializer, SignInSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = str(RefreshToken.for_user(user).access_token)
        return Response({'token': token}, status=status.HTTP_201_CREATED)


class SignInView(generics.GenericAPIView):
    serializer_class = SignInSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'token': serializer.validated_data['token']}, status=status.HTTP_200_OK)


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
