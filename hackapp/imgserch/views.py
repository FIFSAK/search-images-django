from django.shortcuts import render
from .models import Request


# Create your views here.
def index(request):
    return render(request, "imgserch/index.html")


def result(request):
    r = Request.objects.order_by("-id")[:-1]
    return render(request, "imgserch/result.html", {'req': r})
