from django.urls import path

from .views import home, remoteio

urlpatterns = [
    path("", home, name="home"),
    path("/remoteio", remoteio, name="remoteio"),
]
