from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

from django.db import models

# from django.conf import settings
# from django.contrib.sessions.models import Session

class User(AbstractUser):
    pass
    # def __str__(self):
        # return self.username

# class UserSession(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    # session = models.ForeignKey(Session)

class Listing(models.Model):
    category_choices = [
    ('home', 'Home'),
    ('electronics', 'Electronics'),
    ('toys', 'Toys'),
    ('other', 'Other')
]
    title = models.CharField(max_length=254)
    description = models.TextField()
    start_bid = models.FloatField()
    image_url = models.URLField(max_length=254, blank=True)
    category = models.CharField(max_length=254, blank=True, choices=category_choices)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass
