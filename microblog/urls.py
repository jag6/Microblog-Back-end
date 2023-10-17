from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('comments/', CommentListView.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('tags/<int:pk>', TagListView.as_view(), name='tag'),
    path('likes/', LikeListView.as_view(), name='likes'),
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like')
]