from django.shortcuts import render, redirect
from .models import Request
from .forms import RequestForm
import requests
API_KEY = "DuaCuEifyNh8i0cjdYoGt6du82vYVxD3KwaR5sqSxiElaBERgiFgZttg"
ENDPOINT = "https://api.pexels.com/v1/curated"

def index(request):
    r = Request.objects.order_by('id').last()
    if request.method == 'POST':
        form = RequestForm(request.POST)

        if form.is_valid():
            Request.objects.all().delete()
            form.save()
            return redirect('main')

    else:
        form = RequestForm()
    photo_urls = []
    if r:
        photo_urls = get_photo_urls(r.request)
    return render(request, "imgserch/index.html", {'req': r, 'form': form, 'photo_urls': photo_urls})

def get_photo_urls(query):
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": API_KEY}
    params = {"query": query, "per_page": 10}
    response = requests.get(url, headers=headers, params=params)
    photos = response.json()["photos"]
    photo_urls = [
        f"https://images.pexels.com/photos/{photo['id']}/pexels-photo-{photo['id']}.jpeg"
        for photo in photos
    ]
    return photo_urls