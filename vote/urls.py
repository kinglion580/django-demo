from django.urls import path
from vote import views

app_name = 'vote'
urlpatterns = [
    path('', views.index, name='index'),
    path('vote/', views.vote, name='vote'),
    path('query/', views.query, name='query'),
]
