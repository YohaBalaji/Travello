from django.utils.encoding import force_bytes

from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.tokens import default_token_generator 
from .models import users

def get(request):
    User.objects.all()
    for val in User:
        messages.info(request,User.username)
    
    
def logout(request):
    auth.logout(request)
    return redirect('/view')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return HttpResponse('Login!...')
            return redirect('/view')
        else:
            messages.info(request,"Invalid Cradential's")
            return redirect('login')
    else:
        return render(request, 'login.html')


def user(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is Already taken')
                return redirect('user')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Having Another Account with this Email ID')
                return redirect('user')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
                user.save();

                token = default_token_generator.make_token(user)
                print(f"Token created: {token}")
                obj = users(first_name=first_name,last_name=last_name,user_name=username,email =email ,password1=password1,password2=password2,token = token)
                obj.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request, "Password not Matching")
            return redirect('user')
    else:
        return render(request, 'user.html')
