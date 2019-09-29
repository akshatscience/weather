import requests
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import weather
from django.db.models import Q # new

# Create your views here.


def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2ef7677a9f31d3a93404cd663fe966dd'



    cities = weather.objects.all()
    weather_data=[]
    for city in cities:

        r = requests.get(url.format(city)).json()
        city_weather = {
                'city':city,
                'temprature':r['main']['temp'],
                'description':r['weather'][0]['description'],
                'icon':r['weather'][0]['icon']
            }    
        weather_data.append(city_weather)  
    return render(request,'index.html',{'weather_data':weather_data})


def search(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2ef7677a9f31d3a93404cd663fe966dd'


    cities = weather.objects.all()
    for i in cities:
        

        city = weather.objects.get(name = i)

        r = requests.get(url.format(city)).json()


        city_weather = {
                    'city':city,
                    'temprature':r['main']['temp'],
                    'description':r['weather'][0]['description'],
                    'icon':r['weather'][0]['icon']
                }    
        return render(request,'search.html',{'city_weather':city_weather})


    

def get_queryset(self): # new
        return weather.objects.filter(
            Q(name__icontains=weather.objects.all()) | Q(state__icontains='NY')
        )
