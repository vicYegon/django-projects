from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages, redirects

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['first-name']
        lastname = request.POST['last-name']
        username = request.POST['username']
        email = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirm-password']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email already exists')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, email=email, firstname=firstname, 
                                                lastname=lastname)
                user.set_password(password)
                user.save()
                print('successfully registered')
                return redirect('login')
    else:
        return render(request, "register.html")
    

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            return redirect('home')
        else:
            messages.info(request, 'invalid email or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    return render(request, 'home.html')