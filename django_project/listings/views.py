from django.shortcuts import render

from .helpers.listings import (
    get_wwr_listings,
    get_remoteio_listings,
    get_brightermon_listings,
)

# Create your views here.


def home(request):
    return render(request, "home.html")


def remoteio(request):
    listings = get_remoteio_listings()
    return render(request, "listings.html", {"listings": listings})


def wwr(request):
    listings = get_wwr_listings()
    return render(request, "listings.html", {"listings": listings})


def bightermmon(request):
    listings = get_brightermon_listings()
    return render(request, "listings.html", {"listings": listings})
