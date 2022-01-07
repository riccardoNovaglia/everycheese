from django.urls import path
from . import views

app_name = "cheeses"
urlpatterns = [
    path("", views.CheeseList.as_view(), name="list"),
    path("<slug:slug>/", views.CheeseDetails.as_view(), name="details"),
]
