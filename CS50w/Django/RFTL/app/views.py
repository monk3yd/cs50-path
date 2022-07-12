from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# Main function - takes an argument that represents the HTTP request the user
# makes to access our webserver.
def index(request):
    return render(request, "app/index.html")


def greet(request, name):
    # Third arguments is called the context.
    # It has all the information we want to provide to the template
    return HttpResponse(request, "app/greet.html", {
        "name": name.capitalized()
    })
