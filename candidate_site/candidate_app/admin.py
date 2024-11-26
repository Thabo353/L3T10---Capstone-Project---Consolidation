from django.contrib import admin
from .models import Candidate, Policy

# Register Candidate model with custom admin options
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')  # Removed 'description'
    search_fields = ('name',)  # Allow searching by candidate name
    list_filter = ('votes',)  # Add filtering options

# Register Policy model with default admin options
@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Removed 'created_at'
    search_fields = ('title', 'author__name')        # Allow searching by policy title or author name
    list_filter = ('author',)                       # Added a filter for author instead
