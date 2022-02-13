#from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from login.models import Login
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def loginVal(request):
    if request.method == 'POST':
        
        username1 = request.POST['username']
        password1 = request.POST['password']
        if Login.objects.filter(username = username1).exists():
                user = Login.objects.filter(username = username1)[0]
                if user.password == password1:
                    return HttpResponse("Login Successful")
                else:
                    messages.success(request, 'Invalid Credientls')
                    return redirect("/loginVal")
        else:
            messages.success(request,"Register First")
            return render(request,'register.html') 
    
    else:
        return render(request,'login.html')    


def register(request):
    if request.method == 'POST':
        name = request.POST.get('luser')
        email = request.POST.get('lemail')
        password = request.POST.get('lpassword')
        login = Login(username=name, email=email, password=password)
        login.save()
        messages.success(request,"You are Registered Successfully")
    return render(request,'register.html')

