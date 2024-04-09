from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):
    appid_weather = 'key_openweathermap'
    appid_yandex = 'key_yandex'
    headers = {
        'X-Yandex-Weather-Key': appid_yandex
    }
    url_for_geocoding = 'http://api.openweathermap.org/geo/1.0/direct?q={}&appid={}'
    cities = City.objects.all()
    all_cities = []
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    for city in cities:
        res_1 = requests.get(url_for_geocoding.format(city.name, appid_weather))
        for item in res_1.json():
            lat = item['lat']
            lon = item['lon']
        url_yandex = 'https://api.weather.yandex.ru/v2/forecast?lat={}&lon={}'
        res = requests.get(url_yandex.format(lat, lon), headers=headers).json()
        temp = res['yesterday']['temp']
        city_info = {
            'city': city.name,
            'temp': temp
        }
        all_cities.append(city_info)
    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)