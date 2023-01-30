from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth #importing user
from django.contrib import messages
from .models import Inventory
from .forms import BookingForm

# Create your views here.



def index(request):
    if 'username' in request.session:
        return render(request,'index.html') 
    return redirect(login)

def about(request):
    if 'username' in request.session:
        return render(request,'about.html')
    return redirect(login)


def inventory(request):
    dict_inv = {
        'inventory' :Inventory.objects.all()
    }
    if 'username' in request.session:
        return render(request,'inventory.html',dict_inv)
    return redirect(login)
    

def booking(request):
    if request.method=="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')

    form = BookingForm()
    dict_form ={
        'form':form
    }
    if 'username' in request.session:
        return render(request,'booking.html',dict_form)
    return redirect(login)
    

def contact(request):
    if 'username' in request.session:
        return render(request,'contact.html')
    return redirect(login)

    
def register(request): #REGISTER REQUEST
        if request.method == 'POST':
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            username=request.POST["username"]
            email=request.POST["email"]
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
            if password==confirm_password:
                 if User.objects.filter(username=username).exists():
                      messages.info(request,'Username not available!')
                      return redirect(register)
                 elif User.objects.filter(email=email).exists():
                      messages.info(request,'email entered has an existing account please login to access!')
                      return redirect(register)
                 else:
                      user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                      user.set_password(password)
                      user.is_staff=True
                      user.save()
                      
                      return redirect('login')

            else:
             messages.info(request,'Passwords does not match')
             return redirect(register)

            
        else:
             print("This is not post method")
             return render(request,"register.html")

             
def login(request):  #LOGIN REQUEST
     if 'username' in request.session:
        return redirect(index)
     elif request.method == 'POST': 
          username =request.POST['username'] 
          password = request.POST['password'] 
          user = auth.authenticate(username=username, password=password)
          if user is not None: 
               request.session['username'] = username 
               auth.login(request, user) 
               return redirect('home')
          else: 
               messages.info(request,'Invalid Username or Password') 
               return redirect('login') 
     else: 
          return render(request, 'login.html')


def logout(request):  #LOGOUT REQUEST
     if 'username' in request.session:
         request.session.flush()
    #  auth.logout(request) 
     return redirect('login')


