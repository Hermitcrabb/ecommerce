from django.shortcuts import render, redirect
from userauths.forms import UserRegisterform
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

User = settings.AUTH_USER_MODEL


@csrf_exempt

def register_views(request):

    if request.method == "POST":
        form = UserRegisterform(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Hey {username}, Your Accountt was created succesfully")
            new_user = authenticate(username = form.cleaned_data['email'],
                                    password = form.cleaned_data['password1']
                )
            login(request, new_user)
            return redirect("core:index")
    else:
        form = UserRegisterform()
    
    
    context = {
        'form': form,
    }

    return render(request, "userauths/sign-up.html", context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    
    if request.method == "POST":
        email = request.POST.get("email")  
        password = request.POST.get("password")

        try:
           user = User.object.get(email = email)
           user = User.object.get(password = password)
        except:
            messages.warning(request, f"User with {email} does not exist")
            messages.warning(request, f"{password} does not match")
            
        user = authenticate(request, email=email, password = password)

        if user is not None:
            login(request, user)
            messages.success(request ,"you are logged in")
            return redirect("core:index")

        else:
            message.warning(request, "User dosent exist, crate an account.")
    context = {
        
    }   
    return render(request, "userauths/sign.html", context)

