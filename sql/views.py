import os
from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse, FileResponse
from django import forms
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView

from dwebsocket.decorators import accept_websocket, require_websocket
import paramiko
import subprocess

# Create your views here.
from .models import Partnumber


class TestForm(forms.Form):
    pn = forms.fields.CharField()


class FTPForm(forms.Form):
    email = forms.fields.CharField(widget=forms.Textarea)


class UploadDocumentForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'style': 'display:none', 'multiple': True}))
    #file = forms.FileField()


def index(request):
    '''
    if request.POST:
        form = TestForm(request.POST)
        if form.is_valid():
            pn = form.cleaned_data['pn']
            part = Partnumber.objects.filter(partnumber=pn).first()
            boardid = part.boardid.id
            return render(request, 'sql/index.html', {'form': form, 'boardid': boardid})
    else:
        form = TestForm()
    return render(request, 'sql/index.html', {'form': form})
    '''

    form = TestForm()
    upload_form = UploadDocumentForm()
    '''
    if request.POST:
        form = TestForm(request.POST)
        if form.is_valid():
            #pn = request.POST['pn']
            pn = form.cleaned_data['pn']
            part = Partnumber.objects.filter(partnumber=pn).first()
            boardid = part.boardid.id
            return JsonResponse({"boardid": boardid, "status": True})
        #else:
        #    return JsonResponse({"message": form.errors, "status": False})
    '''

    return render(request, 'sql/index.html', {'form': form, 'upload_form': upload_form})


'''
def ajax_test(request):
    if request.POST:
        pn = request.POST["partnumber"]
        return JsonResponse({"msg": "ok", "pn": pn})
'''


def ajax_test(request):
    if request.POST:
        pn = request.POST['partnumber']
        part = Partnumber.objects.filter(partnumber=pn).first()
        boardid = part.boardid.id
        return JsonResponse({"boardid": boardid})


class TestFormView(View):
    board_dict = {}

    def post(self, *args, **kwargs):
        form = TestForm(self.request.POST)
        if form.is_valid():
            pn = form.cleaned_data['pn']
            part = Partnumber.objects.filter(partnumber=pn).first()
            if part:
                boardid = part.boardid.id
                return JsonResponse({"status": True, "boardid": boardid})
            else:
                return JsonResponse({"status": False, "message": "board number doesn't exist"})


class UploadFilesView(View):
    def post(self, request, *args, **kwargs):
        form = UploadDocumentForm(data=request.POST, files=self.request.FILES)
        files = request.FILES.getlist('files')
        print(request.POST['debug'])
        if form.is_valid():
            path = os.path.join(settings.BASE_DIR, 'files')
            for f in files:
                handle_uploaded_file(f, path)
            '''
            for f in files:
                file_path = open(os.path.join(settings.BASE_DIR, 'files', f.name), 'wb')
                print(f, type(f))
                for chunk in f.chunks():
                    file_path.write(chunk)
                file_path.close()
            return HttpResponse('success')
            '''
        return HttpResponse('fail')


def handle_uploaded_file(file, path):
    with open(path + '/' + file.name, 'wb+') as dst:
        for chunk in file.chunks():
            dst.write(chunk)


'''
class UploadFilesView(FormView):
    form_class = UploadDocumentForm
    template_name = 'sql/index.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('files')
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
'''


'''注意上传的文件不能是0kb的大小
def upload_file(request):
    if request.POST:
        form = UploadDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse('ok')
    else:
        form = UploadDocumentForm()
    return render(request, 'sql/index.html', {'upload_form': form})
'''


def download_board(request):
    path = ''
    if request.POST:
        pn = request.POST.get('pn')
        if pn == '':
            return JsonResponse({'status': False, 'msg': 'please fill out pn'})
        else:
            return JsonResponse({'status': True})


def download(request, debug, pn):
    if debug == 'debug':
        file_path = '/Users/kinglion/Documents/inwork/' + pn + '.txt'
    else:
        file_path = '/Users/kinglion/Documents/release/' + pn + '.txt'
    file = open(file_path, 'rb')
    response = FileResponse(file, as_attachment=True)
    return response


def echo(request):
    os.system("python sql/echo.py")
    return HttpResponse('done')
