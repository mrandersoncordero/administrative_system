"""Users models."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from utils.models import AdministrativeSystem

class User(AdministrativeSystem, AbstractUser):
    """User model.
    
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """
    
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with thar email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format: +99999999. Up to 15 digits allowed.'
    )
    phone_number = models.CharField(max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'He;p easily distinguish users and perform queries.'
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )
    
    def __str__(self) -> str:
        """Return username."""
        return self.username
    

    def get_short_name(self) -> str:
        return self.username
