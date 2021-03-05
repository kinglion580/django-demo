from django.urls import path
from . import views

app_name = 'large_file_upload'
urlpatterns = [
    path('', views.index, name='index'),
]