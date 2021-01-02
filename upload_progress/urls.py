from django.urls import path
from .views import Upload, UploadPage

app_name = 'upload_progress'
urlpatterns = [
    path('upload_page/', UploadPage.as_view()),
    path('upload/', Upload.as_view()),
]
