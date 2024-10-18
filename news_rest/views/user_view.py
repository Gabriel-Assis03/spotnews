from rest_framework import viewsets
from news.models import User
from ..serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer