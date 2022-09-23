from cgitb import html
from distutils.log import info
from urllib import response
from django.shortcuts import render
import requests 
from django.http import HttpResponseRedirect
from .forms import API

def form(request):
    if request.method =="POST":
        form=API(request.POST)
        if form.is_valid():
            required_field=form.cleaned_data['required_field']
            response=dict(requests.get("https://api.spacexdata.com/v4/company").json())
            if required_field =="headquarters":
               ans={'ans':response.get("headquarters")}
            if required_field =="links":
               ans={'ans':response.get("links")}
            if required_field =="name":
               ans={'ans':response.get("name")}
            if required_field =="founder":
               ans={'ans':response.get("founder")}
            if required_field =="valuation":
               ans={'ans':response.get("valuation")}
            # if kya_chaiye=='LAUNCHPADS':
            #     response=requests.get("https://api.spacexdata.com/v4/launchpads").json()
            # if kya_chaiye=='ROCKETS':
            #     response=requests.get("https://api.spacexdata.com/v4/rockets").json()
            # if kya_chaiye=='HISTORY':
            #     response=requests.get("https://api.spacexdata.com/v4/history").json()
                    
        return render(request,'outform.html',ans)

    if request.method=="GET":
        form=API()
        input={'form':form}
        return render(request,'inform.html',input)

    