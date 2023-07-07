from django.urls import path

from . import views

urlpatterns = [
    # path("login", views.login, name="login"),
    # path("logincheck", views.logincheck, name="login"),
    path("landingpage", views.landingpage, name="landingpage"),
    path("uploadfile", views.uploadfile, name="uploadfile"),
]