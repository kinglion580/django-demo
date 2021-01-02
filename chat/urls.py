from django.urls import path

from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('get_message', views.get_message, name='get_message'),
    path('<str:room_name>/', views.room, name='room'),
]