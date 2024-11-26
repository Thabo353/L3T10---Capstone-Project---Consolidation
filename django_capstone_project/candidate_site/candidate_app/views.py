from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Candidate, Policy
from django.conf import settings

# Candidate list view
def candidate_list(request):
    """
    Display a list of candidates. If no candidates are available, show a message.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse: Renders the candidate_list.html page with candidates and a message.
    """
    candidates = Candidate.objects.all()
    if not candidates:
        message = "No candidates available at the moment."
    else:
        message = None
    return render(request, 'candidate_app/candidate_list.html', {'candidates': candidates, 'message': message})


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
    If the form is valid, login the user and redirect them to the home page.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('candidate_app:home')  
    else:
        form = AuthenticationForm()

    return render(request, 'candidate_app/login.html', {'form': form})


# Logout view
def logout_view(request):
    """
    Logs the user out and redirects them to the homepage.
    """
    logout(request)
    return redirect('candidate_app:home') 


# Home page view
def home_view(request):
    """
    Render the home page displaying candidate information.
    
    Parameters:
    - request: HttpRequest object.
    
    Returns:
    - HttpResponse: Renders home.html with candidate context.
    """
    candidates = Candidate.objects.all()
    return render(request, 'candidate_app/home.html', {'candidates': candidates})


# To be implemented later 
#def learn_more(request):
    """
    Direct users to either login or register depending on their choice.
    """
    return render(request, 'candidate_app/learn_more.html')


@login_required
def vote(request, candidate_id):
    # Get the candidate object
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    
    # Increment the candidate's vote count
    candidate.votes += 1
    candidate.save()
    
    # Redirect to home page after voting
    return redirect('candidate_app:home')


# To be implemented later
# Policies page view
#def policies(request, candidate_id):
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
    if request.method == 'POST' and request.user.is_authenticated:
        policy_id = request.POST.get('policy_id')
        policy = get_object_or_404(candidate.policies, id=policy_id)
        policy.votes += 1
        policy.save()
        candidate.votes += 1
        candidate.save()
        return redirect('candidate_app:policies', candidate_id=candidate_id)

    return render(request, 'candidate_app/policies.html', {'candidate': candidate, 'policies': policies})
