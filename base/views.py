from django.shortcuts import render, redirect

from geopy.geocoders import Nominatim

def get_coordinates(address):
    # Create a geocoder object
    geolocator = Nominatim(user_agent="my_application")

    # Use geocode function to get the location information of the address
    location = geolocator.geocode(address)

    # Extract the latitude and longitude information from the location object
    latitude = location.latitude
    longitude = location.longitude

    # Return the latitude and longitude as a tuple
    return (latitude, longitude)


def index(request):
    if request.method == 'POST':
        x = (request.POST.get('x'))
        y = (request.POST.get('y'))
        address= (request.POST.get('address'))
        if x and y:
            x=float(x)
            y=float(y)
            return map(request, x=x, y=y)
        elif address:
            (x,y)=get_coordinates(address)
            x=float(x)
            y=float(y)
            return map(request, x=x, y=y)
    return render(request, 'base/index.html')


def map(request, x,y):
    context = {
        'x': x,
        'y': y,
    }
    return render(request, 'base/map.html', context)

def realtime(request):
    return render(request, 'base/realtime.html')

def team(request):
    return render(request,"base/team.html")