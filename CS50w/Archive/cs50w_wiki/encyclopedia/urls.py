from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # redirect path to wiki?
    path("wiki/", views.index, name="wiki"),
    path("wiki/<title>/", views.title, name="title"),
    path("search/", views.search, name='search'),
    path("newpage/", views.newpage, name='newpage'),
    path("editpage/", views.editpage, name='editpage'),
    path("randompage/", views.randompage, name='randompage')
]
