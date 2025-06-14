from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/", views.index, name="index1"),
    path("search/", views.search_redirect, name="search"),  # For form submission

    path("newpage/", views.add, name="add"),
    path("change/<str:title>", views.change, name="change"),
    path("random/", views.random_entry, name="random")
]

