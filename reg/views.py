from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Products
# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 =request.POST['password1']
        password2 = request.POST['password2']    
        if password1 == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request,'Email already Used')
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request,'Username already Used')
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, email=email, password = password1)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password Invalid')
            return redirect('/')
    else:
        return render(request,'signup.html')

            
    
    #return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:    
        return render(request,'login.html')
    
def index(request):
    products = Products.objects.all()
    return render(request,'index.html',{'products':products})

def product(request):
    products = Products.objects.all()
    #products = [product1,product2,product3,product4,product1]
    return render(request,'products.html',{'products':products})

def about(request):
    return render(request,'about.html')



def contacts(request):
    return render(request,'contact.html')


def logout(request):
    auth.logout(request)
    return redirect('index')