from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search_redirect, name="search"),  # For form submission
    path("newpage/", views.add, name="add")
]

