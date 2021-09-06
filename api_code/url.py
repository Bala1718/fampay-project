from django.urls import path

from api_code import views

urlpatterns = [
    path('', views.index, name='index'),
]