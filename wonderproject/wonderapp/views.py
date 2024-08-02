from django.shortcuts import render,redirect
from django.http import HttpResponse

import wonderproject.settings
from .forms import WonderForm
from . models import Wonder
from wonderapp.models import Wonder



def index(request):
    wonder=Wonder.objects.all()
    contex={
        'wonder_list':wonder
    }
    return render(request,'index.html',contex)
def detail(request,wonder_id):
    wonder=Wonder.objects.get(id=wonder_id)
    return render(request,"detail.html",{'wonder':wonder})
def add_wonder(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        wonder=Wonder(name=name,desc=desc,img=img)
        wonder.save()

    return render(request,'add.html')



def update(request,id):
    wonder=Wonder.objects.get(id=id)
    form=WonderForm(request.POST or None,request.FILES,instance=wonder)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'wonder':wonder})
def delete(request,id):
    if request.method=="POST":
        wonder=Wonder.objects.get(id=id)
        wonder.delete()
        return redirect('/')
    return render(request,'delete.html')

