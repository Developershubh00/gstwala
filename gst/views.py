from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid login details")
    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def gst_filing(request):
    if request.method == 'POST':
        # Process GST filing details
        return redirect('payment')
    return render(request, 'gst_filling.html')

def payment(request):
    if request.method == 'POST':
        # Process payment
        return HttpResponse("Payment successful!")
    return render(request, 'payment.html')
