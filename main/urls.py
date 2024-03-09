from django.urls import path
from . import views


urlpatterns = [
    path("<int:id_>", views.index, name="index"),
    path("home/", views.home, name="home"),
]