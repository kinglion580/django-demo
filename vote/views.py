from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from uuid import uuid4
from queue import Queue, Empty
import json

UUUU = {
    '1': {'name': '王', 'count': 1},
    '2': {'name': '李', 'count': 1},
    '3': {'name': '赵', 'count': 1},
}

# 为每个登录用户保存
# dfasdfadsfasdfadf: Queue()
USER_QUEUE_DICT = {

}


def index(request):
    nid = str(uuid4())
    USER_QUEUE_DICT[nid] = Queue()
    request.session['user_info'] = nid
    return render(request, 'vote/index.html', {'user_list': UUUU})


def query(request):
    """每个用户查询最新投票信息"""
    ret = {'status': True, 'data': None}
    current_user_nid = request.session['user_info']
    queue = USER_QUEUE_DICT[current_user_nid]
    try:
        # {'uid':1, 'count':6}
        ret['data'] = queue.get(timeout=10)  # 十秒后断开，再连
    except Empty as e:
        ret['status'] = False
    # return jsonify(ret)
    # json.dumps(ret)
    return JsonResponse(ret)


def vote(request):
    """
    用户投票
    :return:
    """
    #uid = request.args.get('uid')
    uid = request.GET.get('uid')
    old = UUUU[uid]['count']
    new = old + 1
    UUUU[uid]['count'] = new

    for q in USER_QUEUE_DICT.values():
        q.put({'uid': uid, 'count': new})

    return HttpResponse("投票成功")
