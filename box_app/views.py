from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from.models import tabledata

def reg(request):
    return render(request,'box_app/reg.html')

def login_view(request):
    return render(request,'box_app/login.html')

def regsave(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
        
    user = User.objects.create_user(username=name, email=email, password=password)
    user.save()
    return redirect(login_view)
    

def loginsave(request):
    email = request.POST['email']
    password = request.POST['password']
        
    user = authenticate(request,email=email, password=password)
        
    if user is not None :
        login(request, user)
        return redirect(dataentry)
    else:
        return redirect(dataentry)
        # return HttpResponse(email,password)
        return render(request,'box_app/login.html',{'data':'invalid data'})

def dataentry(request):
    return render(request, 'box_app/dataentry.html',{'data':'data'})

def datasave(request):
    
    length = request.POST['length']
    width = request.POST['width']
    height = request.POST['height']
    area = request.POST['area']
    volume = request.POST['volume']
    
    x = tabledata(length=length,width=width,height=height,area=area,volume=volume)
    x.save()
    
    return redirect(dataentry)
    


def table(request):
    
    return render(request, 'box_app/table.html')

def allluser(request):
    x = User.objects.all()
    return render(request, 'box_app/allluser.html',{'data':x})



def table(request):
    
    x = tabledata.objects.all()
    
    return render(request, 'box_app/table.html',{'data':x})

def deleteuser(request):
    
    x = User.objects.get(pk=request.GET['id'])
    x.delete()
    return redirect(allluser)


def delete(request):
    
    x = tabledata.objects.get(pk=request.GET['id'])
    x.delete()
    return redirect(table)


def edit(request):
    
    x = tabledata.objects.get(pk=request.GET['id'])
    length = request.POST['length']
    width = request.POST['width']
    height = request.POST['height']
    area = request.POST['area']
    volume = request.POST['volume']
    
    x = tabledata(length=length,width=width,height=height,area=area,volume=volume)
    x.save()
    
    return redirect(dataentry)
   


def logout(request):
    auth.logout(request)                 
    return redirect(login_view)