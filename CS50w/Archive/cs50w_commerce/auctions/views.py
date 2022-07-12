from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in

# from django.views.generic import CreateView

from .models import User, Listing
from .forms import newListingForm


def index(request):
    listings = Listing.objects.values()
    return render(request, "auctions/index.html", {"listings": listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def newListing(request):
    if request.method == "POST":
        # Create form instance
        form = newListingForm(request.POST)  # (request.POST or None)

        if form.is_valid():
            valid_form = form.save(commit=False)
            valid_form.author = request.user
            valid_form.save()
            messages.success(request, 'Item was added to listing succesfully')
            return redirect('index')

    else:
        form = newListingForm()

    return render(request, "auctions/newListing.html", {"form": form})

# class newListingView(CreateView):
    # def get(self, request):
        # form_class = newListingForm
        # context = {'form': form}
        # return render(request, "auctions/newListing.html", {"form": form})

    # model = Listing

