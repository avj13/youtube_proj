from django.urls import path
from youtube_api import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list", views.get_videos, name="get_video"),

]