from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('comments/', CommentListView.as_view(), name='posts'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='post')
]