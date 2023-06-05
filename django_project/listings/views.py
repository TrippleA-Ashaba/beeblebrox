from django.shortcuts import render

from .helpers.listings import get_wwr_listings, get_remoteio_listings

# Create your views here.


def home(request):
    listings = get_wwr_listings()
    return render(request, "home.html", {"listings": listings})


def remoteio(request):
    listings = get_remoteio_listings()
    return render(request, "remoteio.html", {"listings": listings})
