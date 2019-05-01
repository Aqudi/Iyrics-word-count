from django.shortcuts import render, get_object_or_404
from .models import *
import word_counter.songParser as sp

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request, lyrics_id):
    data = dict()
    data['text_data'] = request.GET['data']
    data['text_data'].encode('cp949')
    # print(check_lyrics_data)
    print(request.GET)
    if 'checkbox' in request.GET:
        sp.save_data(data['text_data'])
        data['lyrics'] = get_object_or_404(lyrics, pk=lyrics_id)
        print("checked!")
    return render(request, 'result.html', data)