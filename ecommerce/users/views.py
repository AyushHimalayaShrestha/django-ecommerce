from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import LoginForms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .auth import redirect_if_logged_in
# Create your views here.

#register view
@redirect_if_logged_in
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

#login view
@redirect_if_logged_in
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
            
                if user.is_staff:
                    return redirect('dashboard_product_lists')
                else:
                    next_url =request.GET.get('next','/')
                    return redirect(next_url)
            
        else:
                messages.error('Login Failed!')

    else:
        form = LoginForms()
        return render(request,'login.html',{'form':form})
    

# logout view
def logout_view(request):
    logout(request)
    messages.success(request,"User Logged Out Successfully!")
    return redirect('login_view')
