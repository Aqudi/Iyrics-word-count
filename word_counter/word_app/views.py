from django.shortcuts import render
import songParser.songParser as sp


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text_data = request.GET['data']
    return render(request, 'result.html', {"data":text_data})


if __name__ == "__main__":
    for s in sp.getData("엔플라잉 옥탑방"):
        print(s.getText())