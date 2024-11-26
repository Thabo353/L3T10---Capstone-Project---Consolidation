from django.db import models

class Candidate(models.Model):
    """
    Represents a candidate in the application with basic details.

    Attributes:
        name (str): The candidate's name, with a maximum length of 100 characters.
        bio (str): A detailed biography of the candidate.
        slogan (str): The candidate's campaign slogan, up to 255 characters.
        description (str): A short description of the candidate.
    """
    name = models.CharField(max_length=100)
    slogan = models.CharField(max_length=255)
    bio = models.TextField()
    description = models.CharField(max_length=255, blank=True, null=True)  
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        Returns the candidate's name as the string representation.
        
        Returns:
            str: The name of the candidate.
        """
        return self.name


class Policy(models.Model):
    """
    Represents a policy created by a candidate.

    Attributes:
        title (str): The title of the policy, with a maximum length of 100 characters.
        content (str): The content or details of the policy.
        author (Candidate): A foreign key referencing the candidate who authored the policy.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='policies')
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        Returns the title of the policy as the string representation.
        
        Returns:
            str: The title of the policy.
        """
        return self.title
