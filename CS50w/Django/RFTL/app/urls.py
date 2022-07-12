from django.urls import path

from . import views

# List of URLs accessible to this particular app
urlpatterns = [
    # The first argument represent the default url route path associated to the view
    # Second argument is the function index from the views.py file.
    # Giving a name to a path can be a useful tool for referencing
    path("", views.index, name="index"),
    path("greet/<str:name>", views.greet, name="greet"),
]