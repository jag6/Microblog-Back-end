from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import *
from .permissions import *


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    
class CreateUserView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class FollowListView(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

class FollowDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsFollowerOrReadOnly)