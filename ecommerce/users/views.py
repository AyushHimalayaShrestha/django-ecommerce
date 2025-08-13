from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import LoginForms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Register Successfully.")
            return redirect('/')
        else:
            messages.error(request,"Something went wrong.")
    else:
        form = UserCreationForm()

    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user= authenticate(request,username=username, password=password)

            if user is not None:
                login(request,user)
                messages.success(request,'Login successful')
                return redirect('/')
            
            else:
                messages.error('Login Failed!')

    else:
        form = LoginForms()
        return render(request,'login.html',{'form':form})
    

