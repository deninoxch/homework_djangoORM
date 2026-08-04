from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_game, name="add_game"),
]