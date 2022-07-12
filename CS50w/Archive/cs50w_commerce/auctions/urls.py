from django.urls import path

# from .views import newListingView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newlisting", views.newListing, name="newListing")
    # path("newlisting", newListingView.as_view(), name="newListing")
]
