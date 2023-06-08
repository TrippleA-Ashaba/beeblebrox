from django.urls import path

from .views import home, remoteio, wwr, bightermmon

urlpatterns = [
    path("", home, name="home"),
    path("wwr/", wwr, name="wwr"),
    path("remoteio/", remoteio, name="remoteio"),
    path("bightermmon/", bightermmon, name="brightermon"),
]
