from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .models import User
from .import views
from .forms import Registration


def index(request):
    if request.method == 'POST':
        fm=Registration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            un=fm.cleaned_data['username']
            pw=fm.cleaned_data['password']
            cp=fm.cleaned_data['confirmpassword']
            md=fm.cleaned_data['mob']
            gd=fm.cleaned_data['gender']
            skill=fm.cleaned_data['skill']
            reg=User(name=nm, username=un, password=pw, confirmpassword=cp, mob=md, gender=gd, skill=skill)
            reg.save()
    else:
        fm=Registration()
    return render(request,'index.html',{'form':fm})

def showdata(request):
    stud = User.objects.all()
    return render(request, 'showdata.html',{'stu': stud})

def delete_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm=Registration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm=Registration(instance=pi)
    return render(request,'update_data.html',{'form':fm})