from django.urls import path
from .views import *


urlpatterns = [
    ### auth/
    path('auth/create/', CreateUserView.as_view(), name='create'),
    path('auth/token/', CreateTokenView.as_view(), name='token'),
     path('auth/change-pw/<int:pk>/', ChangePasswordView.as_view(), name='change-password'),
    path('auth/update-profile/<int:pk>/', UpdateProfileView.as_view(), name='update-profile'),
    ### users/
    path('users/', UserListView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user')
]