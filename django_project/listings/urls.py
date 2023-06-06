from django.urls import path

from .views import home, remoteio, wwr

urlpatterns = [
    path("", home, name="home"),
    path("wwr/", wwr, name="wwr"),
    path("remoteio/", remoteio, name="remoteio"),
]
