from django.db import models

class Candidate(models.Model):
    """
    Represents a candidate in the application with basic details.

    :param name: The candidate's name, with a maximum length of 100 characters.
    :type name: str
    :param slogan: The candidate's campaign slogan, up to 255 characters.
    :type slogan: str
    :param bio: A detailed biography of the candidate.
    :type bio: str
    :param description: A short description of the candidate. Defaults to None.
    :type description: str, optional
    :param votes: The total number of votes the candidate has received. Defaults to 0.
    :type votes: int
    """
    name = models.CharField(max_length=100)
    slogan = models.CharField(max_length=255)
    bio = models.TextField()
    description = models.CharField(max_length=255, blank=True, null=True)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        Returns the candidate's name as the string representation.

        :return: The name of the candidate.
        :rtype: str
        """
        return self.name


class Policy(models.Model):
    """
    Represents a policy created by a candidate.

    :param title: The title of the policy, with a maximum length of 255 characters.
    :type title: str
    :param description: The content or details of the policy.
    :type description: str
    :param author: A foreign key referencing the candidate who authored the policy.
    :type author: Candidate
    :param votes: The total number of votes the policy has received. Defaults to 0.
    :type votes: int
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='policies')
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        Returns the title of the policy as the string representation.

        :return: The title of the policy.
        :rtype: str
        """
        return self.title
