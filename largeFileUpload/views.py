from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import File


class FileCreate(CreateView):
    model = File
    fields = "__all__"
