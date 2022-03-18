from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from TMS_App.forms import ticketForm,AdminForm
from .models import Ticket

# Create your views here.
def login(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        passwd=request.POST.get("pass")
        user=authenticate(username=uname,password=passwd)
        
        if user is not None and user.is_active: 
            auth_login(request,user)
            if user.is_superuser:
                return redirect('/adminpage')
            else:
                return redirect('/home')
        else:
            return HttpResponse("<h2>User not found</h3>")
    return render(request,"login.html")

def signup(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        passwd1=request.POST.get("pass1")
        passwd2=request.POST.get("pass2")
        email=request.POST.get("email")
        if passwd1==passwd2:
            if User.objects.filter(username=uname).exists():
                return HttpResponseRedirect("username already exists ,try with login")
            else:
                user=User.objects.create_user(username=uname,password=passwd1,email=email)
                user.save()
                print("user created")
                return redirect("/")
        else:
            print("passwords not match")        
        
    return render(request,"signup.html")

@login_required
def home(request):
    tickets=Ticket.objects.filter(created_by=request.user)
    form = ticketForm()
    if request.method=="POST":
        if request.POST.get("form"):
            form = ticketForm(request.POST or None)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.created_by = request.user
                obj.save()
                return redirect("/home")
        if request.POST.get("logout"):
            auth_logout(request)
            return redirect("/")
    return render(request,'index.html',{"tickets":tickets,"form":form})


@login_required
def update(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == "POST" :
        form = ticketForm(request.POST or None,instance = ticket)
        if form.is_valid():
            form.save()
            return redirect("/home")
        return render(request, 'edit.html',{'form':form})
    else:
        tickets = Ticket.objects.get(id=id)
        form = ticketForm(instance = tickets)
        return render(request, 'edit.html',{"form":form})
 
 
def admin(request):
    ticket=Ticket.objects.all().order_by('-modified')
    if request.method=="POST":
        if request.POST.get("logout"):
            auth_logout(request)
            return redirect("/")
    return render(request,'adminpage.html',{'ticket':ticket})

def adminupdate(request,id):
    tickets = Ticket.objects.get(id=id)
    if request.method == "POST" :
        form = AdminForm(request.POST or None,instance = tickets)
        print(form.errors.as_data())
        if form.is_valid():
            form.save()
            return redirect("/adminpage")
        return render(request, 'adminedit.html',{'form':form})
    else:
        tickets = Ticket.objects.get(id=id)
        form = AdminForm(instance = tickets)
        return render(request, 'adminedit.html',{"form":form})
