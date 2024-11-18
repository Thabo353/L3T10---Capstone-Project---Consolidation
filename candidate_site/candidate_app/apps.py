from django.apps import AppConfig

class WebsiteAppConfig(AppConfig):
    """
    Configuration for the candidate application.

    Attributes:
        default_auto_field (str): Specifies the type of primary key to use for models in this app.
        name (str): The name of the application, used for Django's app registry.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'candidate_app'

