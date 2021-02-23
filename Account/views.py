from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import User
from django.contrib.auth import authenticate, login, get_user_model, logout



# Create your views here.


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)

    context = {
        "login_form": login_form
    }

    if login_form.is_valid():
        print(login_form.cleaned_data)
        
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد')



    return render(request, 'account/login.html', context)




from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    register_form = RegisterForm(request.POST or None)

    context = {
        "title": "Register page",
        "content": "this is Register page",
        "register_form": register_form,
    }

    if register_form.is_valid():
        print(register_form.cleaned_data)
        user_name = register_form.cleaned_data.get('user_name')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username=user_name, email=email, password=password)

        return redirect('/h/login')



    return render(request, 'account/register.html', context)

    
