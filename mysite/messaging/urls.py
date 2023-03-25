from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path("bro1/",views.client1)
]
