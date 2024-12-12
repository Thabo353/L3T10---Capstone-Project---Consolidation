"""
Handles the primary views of the candidate_app including candidate listing, user authentication,
home page display, and voting functionality.

:param request: HttpRequest object representing the HTTP request.
:type request: HttpRequest
:param candidate_id: ID of the candidate (used in views that require it), defaults to None.
:type candidate_id: int, optional
:return: HttpResponse for the respective views.
:rtype: HttpResponse
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Candidate, Policy
from django.conf import settings

def candidate_list(request):
    """
    Displays a list of candidates. If no candidates are available, shows a default message.

    :param request: HttpRequest object representing the HTTP request.
    :type request: HttpRequest
    :return: Renders the candidate list page with candidates and optional message.
    :rtype: HttpResponse
    """
    candidates = Candidate.objects.all()
    message = "No candidates available at the moment." if not candidates else None
    return render(request, 'candidate_app/candidate_list.html', {'candidates': candidates, 'message': message})

def register(request):
    """
    Handles user registration. Processes the UserCreationForm and registers a user on success.

    :param request: HttpRequest object representing the HTTP request.
    :type request: HttpRequest
    :return: Renders the registration page or redirects to the home page on success.
    :rtype: HttpResponse
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

def user_login(request):
    """
    Handles user login. Validates the login form and logs in the user on success.

    :param request: HttpRequest object representing the HTTP request.
    :type request: HttpRequest
    :return: Renders the login page or redirects to the home page on successful login.
    :rtype: HttpResponse
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

def logout_view(request):
    """
    Logs out the user and redirects them to the home page.

    :param request: HttpRequest object representing the HTTP request.
    :type request: HttpRequest
    :return: Redirects to the home page.
    :rtype: HttpResponse
    """
    logout(request)
    return redirect('candidate_app:home')

def home_view(request):
    """
    Displays the home page with a list of candidates.

    :param request: HttpRequest object representing the HTTP request.
    :type request: HttpRequest
    :return: Renders the home page with candidate data.
    :rtype: HttpResponse
    """
    candidates = Candidate.objects.all()
    return render(request, 'candidate_app/home.html', {'candidates': candidates})

@login_required
def vote(request, candidate_id):
    """
    Handles voting for a specific candidate. Requires user authentication.

    :param request: HttpRequest object representing the HTTP request.
    :type request: HttpRequest
    :param candidate_id: The ID of the candidate to vote for.
    :type candidate_id: int
    :return: Redirects to the home page after voting.
    :rtype: HttpResponse
    """
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    candidate.votes += 1
    candidate.save()
    return redirect('candidate_app:home')

def policies(request, candidate_id):
    """
    Displays the policies for a specific candidate. Allows voting for individual policies if the user is authenticated.

    :param request: HttpRequest object representing the HTTP request.
    :type request: HttpRequest
    :param candidate_id: The ID of the candidate whose policies are displayed.
    :type candidate_id: int
    :return: Renders the policies page with candidate and policy data.
    :rtype: HttpResponse
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
