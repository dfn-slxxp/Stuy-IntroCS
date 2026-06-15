from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("add/", views.submit),
    path("farms/", views.farms),
    path("quiz/", views.quiz)
]