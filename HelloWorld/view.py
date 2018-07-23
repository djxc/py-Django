from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

def hello(request):
    context = {}
    context['hello'] = "I love xc"
    return render(request, 'hello1.html', context)

def ajax(request):     
    if request.method == "GET":
            name = request.GET.get('name')
            result = "ddj!" + str(name)
            return HttpResponse(result)
        
@csrf_exempt         
def ajaxPost(request):     
    if request.method == "POST":
#            env =json.loads(request.POST['name1'])
#            name = request.POST.get('name1')
#            result = "XC!" + str(name)
            param= json.loads(request.body.decode('utf-8'))
            name = param['namep']            
            return HttpResponse("df" + str(name))
        
def getGeojson(request):
    return render(request, 'contry.geojson')
