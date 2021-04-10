from django.shortcuts import render
import sys
from subprocess import run, PIPE
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

# Create your views here.


def index(request):

    return render(request, 'health/home.html')


def brain(request):

    return render(request, 'brain/brain.html')


@csrf_exempt
def scrabble(request):
    inp = request.POST.get('param')
    out = run([sys.executable, 'C:\\Users\\jayit\\Downloads\\medbay\\Brain Games Microservice\\py_scrabble_gui_j\\py_scrabble.pyw'],
              shell=True, stdout=PIPE)
    print(out)
    return render(request, 'brain/brain.html', {'data1': out.stdout})


@csrf_exempt
def fourinrow(request):
    inp = request.POST.get('param')
    out = run([sys.executable, 'C:\\Users\\Jayit\\Downloads\\medbay\\Brain Games Microservice\\4inrow.py'],
              shell=True, stdout=PIPE)
    print(out)
    return render(request, 'brain/brain.html', {'data1': out.stdout})


@csrf_exempt
def connect4(request):
    inp = request.POST.get('param')
    out = run([sys.executable, 'C:\\Users\\Jayit\\Downloads\\medbay\\Brain Games Microservice\\connect4_ai.py'],
              shell=True, stdout=PIPE)
    print(out)
    return render(request, 'brain/brain.html', {'data1': out.stdout})


@csrf_exempt
def game(request):
    inp = request.POST.get('param')
    out = run([sys.executable, 'C:\\Users\\Jayit\\Downloads\\medbay\\Brain Games Microservice\\game.py'],
              shell=True, stdout=PIPE)
    print(out)
    return render(request, 'brain/brain.html', {'data1': out.stdout})


@csrf_exempt
def slide_game(request):
    inp = request.POST.get('param')
    out = run([sys.executable, 'C:\\Users\\Jayit\\Downloads\\medbay\\Brain Games Microservice\\slide_game'],
              shell=True, stdout=PIPE)
    print(out)
    return render(request, 'brain/brain.html', {'data1': out.stdout})


@csrf_exempt
def game1(request):
    inp = request.POST.get('param')
    out = run([sys.executable, 'C:\\Users\\Jayit\\Downloads\\medbay\\Brain Games Microservice\\game1'],
              shell=True, stdout=PIPE)
    print(out)
    return render(request, 'brain/brain.html', {'data1': out.stdout})
