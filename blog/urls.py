from . import views
from django.urls import path
from .views import post_summary

urlpatterns = [
    path("", post_summary, name="home"),
]