"""
URL configuration for the `candidate_site` project.

The `urlpatterns` list routes URLs to views. For more information, see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
    Function views:
        1. Add an import: `from my_app import views`
        2. Add a URL to urlpatterns: `path('', views.home, name='home')`
    Class-based views:
        1. Add an import: `from other_app.views import Home`
        2. Add a URL to urlpatterns: `path('', Home.as_view(), name='home')`
    Including another URLconf:
        1. Import the `include()` function: `from django.urls import include, path`
        2. Add a URL to urlpatterns: `path('blog/', include('blog.urls'))`

:param admin: The Django admin interface.
:type admin: module
:param include: The function to include other URL configurations.
:type include: function
:return: The URL patterns configured for the project.
:rtype: list
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('candidate_app.urls')),
]
