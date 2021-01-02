import os
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.conf import settings


# Create your views here.
class UploadPage(View):
    def get(self, request):
        return render(request, 'upload_progress/index.html')


class Upload(View):
    def post(self, request):
        files = request.FILES.getlist('file')
        for file in files:
            self.handle_uploaded_file(file)
        return HttpResponse('done')

    def handle_uploaded_file(self, f):
        tmp = os.path.join(settings.BASE_DIR, 'files')
        with open(tmp + '/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
