from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from store.forms import CustomUserForm

def register(request):
    """
    Handles user registration.
    Displays registration form and processes POST request to create a new user.
    """
    if request.user.is_authenticated:
        return redirect('/')
        
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('/login')
        else:
            messages.error(request, "Registration failed. Please check the errors below.")
            
    context = {'form': form}
    return render(request, "store/auth/register.html", context)


def loginpage(request):
    """
    Handles user login.
    Authenticates user and starts a session.
    """
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")
        return redirect('/')
        
    if request.method == 'POST':
        name = request.POST.get('username')
        passwd = request.POST.get('password')

        user = authenticate(request, username=name, password=passwd)

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome back! Successfully logged in.")
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/login')
            
    return render(request, "store/auth/login.html")


def logoutpage(request):
    """
    Handles user logout and terminates the session.
    """
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Successfully logged out.")
    return redirect("/")