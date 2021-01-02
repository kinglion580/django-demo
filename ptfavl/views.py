import os
import time
import uuid
import queue
import subprocess
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.cache import cache

# Create your views here.

#QUEUE_DICT = {}


def index(request):
    user_uuid = str(uuid.uuid4())
    q = queue.Queue()
    cache.set(user_uuid, q)
    #q = QUEUE_DICT[user_uuid] = queue.Queue()
    request.session['current_user'] = user_uuid

    q.put("hello world")
    q.put('second string')

    return render(request, 'ptfavl/index.html')


def execute(request):
    user_uuid = request.session['current_user']
    #q = QUEUE_DICT[user_uuid]
    q = cache.get(user_uuid)

    if request.POST:
        q.put("checking...")
        #run_cmd('python ptfavl/echo.py', q)
        run_cmd('ping -c 10 github.com', q)
        q.put("output1...")
        q.put("output2...")
        q.put("output3...")
        q.put("done")
        return JsonResponse({'a': 'b'})


def get_message(request):
    user_uuid = request.session['current_user']
    #q = QUEUE_DICT.get(user_uuid)
    q = cache.get(user_uuid)

    message = q.get()

    return HttpResponse(message)


def run_cmd(shell_cmd, q):
    cmd = shell_cmd.split()
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline().strip()
        if line:
            print('Subprogram output: [{}]'.format(line.decode('utf-8')))
            q.put('Subprogram output: [{}]'.format(line.decode('utf-8')))
    if p.returncode == 0:
        print('Subprogram success')
    else:
        print('Subprogram failed')
