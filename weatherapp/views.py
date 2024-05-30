from django.http import HttpResponse
from django.shortcuts import render
import requests

def Home(request):

   if request.method=="POST":
      city= request.POST.get('city','mumbai')
   else:
      city='mumbai'

   appid = 'e5f4463300087b7a67993b5de9fc2055'
   URL= 'https://api.openweathermap.org/data/2.5/weather'
   PARAMS ={'q':city, 'appid':appid, 'units':'metric'} 
   r=requests.get(url=URL, params=PARAMS)
   res=r.json()
   temp= res['main']['temp']
   description=res['weather'][0]['description']
   #icon=res['weather'][0]['icon']
   return render(request,"weatherapp/index.html", {'description':description,'temp':temp})
