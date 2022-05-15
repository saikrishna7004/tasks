from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# Index Handler
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html", {"active": "home"})
                
# Login Handler
def loginUser(request):
    if request.method != "POST":
        return HttpResponse("Invalid Method")
    username = request.POST.get("username")
    password = request.POST.get("password")
    rememberme = request.POST.get("rememberme")
    if not rememberme:
        request.session.set_expiry(0)
    else:
        request.session.set_expiry(86400)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        messages.add_message(request, messages.SUCCESS, 'Login Successfull')
        return redirect("/")
    messages.add_message(request, messages.ERROR, 'Invalid Username or Password')
    return redirect("/login")

# Login View
def loginView(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, "login.html")

# Logout Handler
def logoutUser(request):
    logout(request)
    return redirect("/")

# About page, for illustrative purpose only
def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "about.html", {"active": "about"})