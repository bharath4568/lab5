from django.urls import path

from . import views

urlpatterns = [
    path('', views.json_response, name='json_response'),
]