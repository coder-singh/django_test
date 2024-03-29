from django.shortcuts import render
from .models import ToDoList


# Create your views here.
def index(response, id_):
    ls = ToDoList.objects.get(id=id_)
    return render(response, "main/base.html", {"name": ls.name})


def home(response):
    return render(response, "main/home.html", {})
