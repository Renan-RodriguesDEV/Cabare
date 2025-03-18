from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.index,
        name="index",
    ),
    path("login/", views.login, name="login"),
    path("about/", views.accounts, name="about"),
    path("contact/", views.contact, name="contact"),
    path("galery/", views.galery, name="galery"),
    path("videos/", views.videos, name="videos"),
    path("meetings/", views.meetings, name="meetings"),
]
