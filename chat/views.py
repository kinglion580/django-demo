import subprocess
import uuid
import queue
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

QUEQUE_DICT = {}
user_uuid = str(uuid.uuid4())
q = QUEQUE_DICT[user_uuid] = queue.Queue()


def index(request):

    request.session['current_user_uuid'] = user_uuid

    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


def test(request):
    #shell_cmd = 'python chat/echo.py'
    #run_cmd(shell_cmd)
    myid = 'yel2'
    #print(request.session.get('username'))

    #request.session['current_user_uuid'] = user_uuid

    q.put('===start output====\n')

    run_cmd('python chat/echo.py')
    q.put('finish')

    return render(request, 'chat/index.html', {'myid': myid})


def run_cmd(shell_cmd):
    cmd = shell_cmd.split()
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline().strip()
        if line:
            print('Subprogram output: [{}]'.format(line.decode('utf-8')))
            #q.put('Subprogram output: [{}]\n'.format(line.decode('utf-8')))
    if p.returncode == 0:
        print('Subprogram success')
    else:
        print('Subprogram failed')


def get_message(request):
    try:
        message = q.get(timeout=1)
    except queue.Empty:
        message = 'done'
    return HttpResponse(message)

