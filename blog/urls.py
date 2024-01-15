from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('session/', views.SessionList.as_view(), name='session_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<str:tag>/', views.CategoryTag.as_view(), name='category_tag'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'), 
]