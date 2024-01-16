from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('session/', views.SessionList.as_view(), name='session_detail'),
    path('spot/', views.SpotList.as_view(), name='spot_tag'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'), 
]