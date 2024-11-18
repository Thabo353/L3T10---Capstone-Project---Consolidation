from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from .models import Candidate, Policy
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create views.

# Registration view
def register(request):
    """
    Handle user registration.

    If the request is POST, it processes the UserCreationForm. 
    If the form is valid, the new user is saved, logged in, and redirected to the home page.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse: Renders the register.html page with the registration form.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('candidate_app:home')
    else:
        form = UserCreationForm()
    return render(request, 'candidate_app/register.html', {'form': form})


# Login view
def user_login(request):
    """
    Handle user login.

    If the request is POST, it processes the AuthenticationForm. 
    If the form is valid, the user is logged in and redirected to the home page.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse: Renders the login.html page with the authentication form.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'candidate_app/login.html', {'form': form})


# Home page view
def home_view(request):
    """
    Render the home page displaying candidate information.
    
    Parameters:
    - request: HttpRequest object.
    
    Returns:
    - HttpResponse: Renders home.html with candidate context.
    """
    candidate = Candidate.objects.first()
    context = {
        'learn_more_redirect': settings.LEARNMORE_REDIRECT,
    }
    return render(request, 'candidate_app/home.html', {'candidate': candidate})

# Policies page view
def policies(request, candidate_id):
    """
    View to display the policies of a specific candidate.
    
    Parameters:
    - request: HttpRequest object
    - candidate_id: ID of the candidate whose policies are to be displayed
    
    Returns:
    - HttpResponse: Renders the policies page for the specific candidate
    """
    candidate = get_object_or_404(Candidate, id=candidate_id)
    policies = Policy.objects.filter(author=candidate)
    return render(request, 'candidate_app/policies.html', {'candidate': candidate, 'policies': policies})
