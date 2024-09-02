from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.
def monthly_challenges(request,month):
    challenge = None
    if month == "january":
        challenge ="Eat no meat for the entire month"
    elif month == "february":
        challenge = "walk for at least 20 minutes every day!"
    elif month =="march":
        challenge = "learn django for at least 20 minutes every day"  
    else:
        return  HttpResponseNotFound("page is not found 404")  

    return HttpResponse(challenge)
