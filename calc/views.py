from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    # return HttpResponse("<h1>hello World<h1>")
    return render(request, 'home.html',{'name':'Balaji'})

def add(request):
    first = int(request.POST['num1'])
    second = int(request.POST['num2'])
    sum = first + second
    return render(request, 'result.html',{'result': sum,'first':first,'second':second})