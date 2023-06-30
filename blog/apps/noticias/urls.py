from django.urls import path
from . import views

app_name = 'noticias'

#url de app noticias
urlpatterns = [
    path('', views.inicio, name="inicio"),


]