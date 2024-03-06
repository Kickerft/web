from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, "authenticate/home.html", {})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Create the user
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname  # Set first name
        myuser.last_name = lastname    # Set last name
        myuser.save()

        messages.success(request, 'Your account has been successfully created')
        return redirect("signin")  # Redirect to the signin page

    return render(request, "authenticate/signup.html", {})

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to the home page
        else:
            messages.error(request, "Wrong password or username")
            return redirect("home")  # Redirect back to the home page

    return render(request, "authenticate/signin.html", {})

def signout(request):
    # Implement sign-out functionality here
    # For example: logout(request)
    return redirect("home")  # Redirect to the home page

# Create your views here.
