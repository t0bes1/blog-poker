from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('session/', views.SessionDetail.as_view(), name='session_detail'),
    path('tag/<str:tag>', views.CategoryTag, name='cat_tag'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'), 
]