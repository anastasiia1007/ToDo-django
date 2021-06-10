from django.shortcuts import render #метод
from .models import *
#from django.http import HttpResponse #класс
#def index(request):
 #   return render(request, 'todolist/index.html')
from django.shortcuts import render
from .models import*

def forma(request):
    return render(request, 'todolist/forma.html', )

def submit(request):
    obj = stroka()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.save()
    mydictionary = {
        "alltodos" : stroka.objects.all()
    }
    return render(request,'todolist/list.html',context=mydictionary)

def delete(request,id):
    obj = stroka.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "alltodos" : stroka.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

def list(request):
    mydictionary = {
        "alltodos" : stroka.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

def sortdata(request):
    mydictionary ={
        "alltodos" : stroka.objects.all().order_by('-priority')
    }
    return render(request,'list.html',context=mydictionary)

def searchdata(request):
    q = request.GET['query']
    mydictionary = {
        "alltodos" : stroka.objects.filter(title__contains=q)
    }
    return render(request,'list.html',context=mydictionary)

def edit(request,id):
    obj = stroka.objects.get(id=id)
    mydictionary = {
        "title" : obj.title,
        "description" : obj.description,
        "priority" : obj.priority,
        "id" : obj.id
    }
    return render(request,'edit.html',context=mydictionary)


def update(request,id):
    obj = stroka(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at = updated_at
    obj.save()
    mydictionary = {
        "alltodos" : stroka.objects.all()
    }
    return render(request,'list.html',context=mydictionary)
