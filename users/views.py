"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Exception
from django.db.utils import IntegrityError

# Model
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm
from users.forms import SignUpForm

# Create your views here.

@login_required
def update_profile(request):
    """Update a user's profile view"""

    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm( request.POST, request.FILES )

        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            if data['picture'] != None:
                profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render( 
        request = request, 
        template_name = 'users/user_update.html',
        context = {
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )

def login_view(request):
    """Login view."""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
        
    return render(request, "users/login.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render( 
        request = request,
        template_name = 'users/signup.html',
        context = {
            'form': form
        }
    )