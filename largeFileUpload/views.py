from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic.edit import CreateView
from .models import File

import json


class FileCreate(CreateView):
    model = File
    fields = "__all__"

    def form_valid(self, form):
        form.save()
        return JsonResponse({'status': 'uploaded'})

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        return HttpResponse(data)
