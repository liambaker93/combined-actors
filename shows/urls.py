from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows, name="shows"),
    path('add_show/', views.addNewShow, name="add_show"),
]
