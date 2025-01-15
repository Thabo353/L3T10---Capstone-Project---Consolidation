"""
URL configuration for the `candidate_app` application.

The `urlpatterns` list routes URLs to the corresponding views within the app. This module defines the structure 
and routing logic for handling various HTTP requests.

For more information, see Django's URL dispatcher documentation:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
    Function-based views:
        1. Add an import: `from my_app import views`
        2. Add a URL to urlpatterns: `path('', views.home, name='home')`

    Class-based views:
        1. Add an import: `from other_app.views import Home`
        2. Add a URL to urlpatterns: `path('', Home.as_view(), name='home')`

    Including another URLconf:
        1. Import the `include()` function: `from django.urls import include, path`
        2. Add a URL to urlpatterns: `path('blog/', include('blog.urls'))`

Attributes:
    app_name (str): The namespace for the `candidate_app` application.
    urlpatterns (list): A list of `path()` instances mapping URLs to their respective views.
"""

from django.urls import path
from django.contrib.auth.views import LogoutView  # Import Django's built-in logout view
from . import views

app_name = 'candidate_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('candidates/', views.candidate_list, name='candidate_list'),
    # path('policies/<int:candidate_id>/', views.policies, name='policies'),  # To be implemented later
    # path('learn-more/', views.learn_more, name='learn_more'),  # To be implemented later
    path('vote/<int:candidate_id>/', views.vote, name='vote'),
]
