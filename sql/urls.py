from django.urls import path

from . import views

app_name = 'sql'
urlpatterns = [
    path('', views.index, name='index'),
    path('ajax', views.ajax_test, name='ajax'),
    path('test', views.TestFormView.as_view(), name='test'),
    path('upload', views.UploadFilesView.as_view(), name='upload'),
    path('download_board', views.download_board, name='download_board'),
    path('download/<debug>/<pn>', views.download, name='download'),
]