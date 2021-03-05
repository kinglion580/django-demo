from django.shortcuts import render
from django.http import HttpResponse
from .forms import *


def index(request):
    file_form = FileForm()
    if request.method == 'POST':
        return HttpResponse('ok')
    else:
        return render(request, 'large_file_upload/index.html', {'file_form': file_form})