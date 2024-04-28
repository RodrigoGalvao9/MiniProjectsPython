from django.shortcuts import render
from . import views
from django.urls import path
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

urlpatterns = [
    path("", views.index, name="index"),
]


