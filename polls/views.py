from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Files
from django.core.files import File
from django.conf import settings
from django.http import FileResponse
import os
# Create your views here.

def index(request):
    return render(request,'polls/index.html')

def findand(request):
    #print(request)
    return render(request,'polls/user.html',{'title':'Поиск файла'})

def my_image(request):
    #image_data = open("/home/entis/favicon.ico", "rb").read()
    return HttpResponse('')

def find(request):
    if request.method == 'GET':
        #print(request.GET.get('param_name'))
        File = Files.objects.all()
        res=""
        for item in File:
            if str(request.GET.get('text')) in item.descr:
                res+=f'<p>{item.filename}<input type="button" value="Скачать" onclick="download(\'{item.pk}\')"></p>\n<p>{item.descr}</p><hr>'
        #return HttpResponse("Hello, "+request.GET.get('text'))
        return HttpResponse(res)

def download(request):
    if request.method == 'GET':
        iid=request.GET.get('id')
        File = Files.objects.all()
        pat=""
        for item in File:
            if item.pk==int(iid):
                pat=item.cont
                item.downCount=item.downCount+1
                item.save()
                #res=HttpResponse(open(settings.BASE_DIR+pat.url,'rb').read(),content_type="application/polls")
                #res['Content-Disposition']='inline;filename='+os.path.basename(settings.BASE_DIR+pat.url)
                #return res
        return HttpResponse("no")
    
    #if request.method == 'GET':
        #iid=request.GET.get('id')
        #File = Files.objects.all()
        #pat=""
        #for item in File:
           # if item.pk==int(iid):
               # pat=item.cont
                #item.downCount=item.downCount+1
               # item.save()
                #return 
        #return HttpResponse(pat)