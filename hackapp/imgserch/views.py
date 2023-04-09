from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "imgserch/index.html")

def result(request):
    return render(request, "imgserch/result.html")
