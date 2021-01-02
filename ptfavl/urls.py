from django.urls import path
from ptfavl import views

app_name = 'ptfavl'
urlpatterns = [
    path('', views.index, name='index'),
    path('execute', views.execute, name='execute'),
    path('get_message', views.get_message, name='get_message'),
]