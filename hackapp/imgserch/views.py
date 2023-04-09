from django.shortcuts import render
from .models import Request


# Create your views here.
def index(request):
    r = Request.objects.all()

    return render(request, "imgserch/index.html", {'req': r})


def result(request):
    return render(request, "imgserch/result.html")
