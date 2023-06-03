from django.shortcuts import render

from .helpers.listings import get_wwr_listings

# Create your views here.


def home(request):
    listings = get_wwr_listings()
    return render(request, "home.html", {"listings": listings})
