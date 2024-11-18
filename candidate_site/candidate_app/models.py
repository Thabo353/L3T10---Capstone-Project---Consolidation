from django.db import models

class Candidate(models.Model):
    """
    Represents a candidate in the application with basic details.

    Attributes:
        name (str): The candidate's name, with a maximum length of 100 characters.
        bio (str): A detailed biography of the candidate.
        campaign_slogan (str): The candidate's campaign slogan, up to 255 characters.
    """
    name = models.CharField(max_length=100)
    bio = models.TextField()
    campaign_slogan = models.CharField(max_length=255)

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
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the title of the policy as the string representation.
        
        Returns:
            str: The title of the policy.
        """
        return self.title
    
food_safety_policy = Policy(
    title="Food Safety and Quality Assurance",
    content="""
        We are committed to maintaining the highest standards of food safety and quality throughout 
        our supply chain. All produce undergoes rigorous testing and complies with local and 
        international safety regulations to ensure that consumers receive the freshest, safest products.
    """,
    
)