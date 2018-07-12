from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = "I love xc"
    return render(request, 'hello.html', context)
