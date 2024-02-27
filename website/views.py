from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    #Check to see if user is login in
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        
        #Authenicate User
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged In")
            return redirect('home')
        else:
            messages.error(request, "There was an error login in Please try again")
            return redirect('home')
    
    else:
        return render(request, 'home.html', {})


# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
        #Authenticate and Login
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        
        user = authenticate(username = username, password = password)
        login(request, user)
        messages.success(request, "You have Successfully registered")
        return redirect('home')

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

