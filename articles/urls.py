from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.board_write, name='write')
]