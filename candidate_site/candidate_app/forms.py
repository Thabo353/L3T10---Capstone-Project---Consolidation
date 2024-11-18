from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    """
    Handles user registration by rendering a registration form and saving a new user.

    Parameters:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: A response to render the registration form page.
        Redirect: Redirects to the login page if the registration is successful.

    Example:
        To register a new user, submit a POST request with 'username', 'password1', and 'password2' to this view.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})