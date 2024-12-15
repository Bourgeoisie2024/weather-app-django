import urllib.request
import json
from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=d3da4b1511d66ef90050c2f7b8cc3923').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
            # Additional data points
            'wind_speed': str(list_of_data['wind']['speed']) + ' m/s', # Wind speed
            'wind_direction': str(list_of_data['wind']['deg']) + '°', # Wind direction
            'visibility': str(list_of_data['visibility']) + ' m', # Visibility
            'sunrise': str(list_of_data['sys']['sunrise']), # Sunrise time (in Unix timestamp)
            'sunset': str(list_of_data['sys']['sunset']), # Sunset time (in Unix timestamp)
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
