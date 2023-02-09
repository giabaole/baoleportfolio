from django.shortcuts import render
from .models import City
import requests
from .forms import CityForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    cities = City.objects.all()

    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = "fd3500ef905fb79655acfc200483c1fa"

    url = base_url + "q={}" + "&units=metric" + "&APPID=" + api_key

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate
        
    form = CityForm()
    city = cities.last()
    city_weather = requests.get(url.format(city)).json()

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    context = {'weather_data': weather, 'form': form}
    
    return render(request, "portfolio/index.html", context)
    # return HttpResponseRedirect(reverse('portfolio:index'))
    
