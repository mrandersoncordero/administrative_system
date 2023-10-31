"""Profile model."""

# Django
from django.db import models

# Utilities
from utils.models import AdministrativeSystem

class Profile(AdministrativeSystem):
    """Profile model.
    
    A profile holds a use's public data like biography, picture, and statictics.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=500, blank=True)

    def __str__(self) -> str:
        """Return user's representation."""
        return str(self.user)