from django.shortcuts import render, get_object_or_404
import songParser as sp
from .models import lyrics
import time
# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def loading(request):
    data_pass = dict()
    print("loading : ", request.GET)
    # 받아온 데이터들로 dict를 새로 구성
    for t, d in request.GET.items():
        data_pass[t] = d
    # checkbox데이터가 포함되었는지 확인
    if 'checkbox' in data_pass:
        data_pass['check_ex'] = True
    else:
        data_pass['check_ex'] = False
    print(data_pass)
    return render(request, "loading.html", data_pass)


def result(request):
    data_pass = dict()
    data_pass["data"] = request.GET['text']
    objects = lyrics.objects.all()
    input_name = data_pass['data']
    id = 0
    for object_l in objects:
        id += 1
        if object_l.name in input_name:
            data_pass['lyrics'] = object_l
    if 'lyrics' not in data_pass.keys():
        sp.save_data(data_pass['data'])
        print("데이터를 받습니다.")
        data_pass['lyrics'] = get_object_or_404(lyrics, pk=id)
    data_pass['name'] = data_pass['lyrics'].name
    words = data_pass['lyrics'].lyrics.split()[:-4]
    data_pass['lyrics'] = data_pass['lyrics'].lyrics.split("\n")
    data_pass['total'] = len(data_pass['lyrics'])

    word_dict = dict()
    for word in words:
        if word in word_dict:
            # Increase
            word_dict[word] += 1
        else:
            # add to the dictionary
            word_dict[word] = 1
    data_pass['word_dict'] = word_dict.items()
    time.sleep(1)
    return render(request, 'result.html', data_pass)


def result2(request):
    data_pass = dict()
    data_pass["data"] = request.GET['text']
    words = data_pass["data"].split()

    word_dict = dict()
    for word in words:
        if word in word_dict:
            # Increase
            word_dict[word] += 1
        else:
            # add to the dictionary
            word_dict[word] = 1
    data_pass['word_dict'] = word_dict.items()

    return render(request, 'result2.html', data_pass)
