from django.urls import path
from .views import FileCreate


app_name = 'largeFileUpload'
urlpatterns = [
    path('', FileCreate.as_view(), name='index'),
]