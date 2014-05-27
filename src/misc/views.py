from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import transaction
from django.conf import settings


def home(request):
    errors = []
    return render_to_response('home.html',{'errors':errors})



def displayThePath(request):
    pseudo_name =  request.GET.get('pseudo_name',None) 
    errors = []
    if pseudo_name:
        migrant = Migrant.objects.get(pseudo=pseudo_name)
        if migrant:
            checkpoints = CheckPoint.objects.filter(migrante=migrant)
            return render_to_response('display_migrant_location.html',{'migrant':migrant,'checkpoints':checkpoints,'errors':errors})
        else:
            #error, just say migrant doesnt exist
            errors.append['Pseudo name not found. Please enter a valid one.']
            #log, the guy who searched, ip, pseudo name, type of search
            #might required in future for showing captcha or banning
            return render_to_response('home.html',{'errors':errors})
    else:
        #error: please enter a pseudo name
        errors.append['Please enter a valid Pseudo name']
        #log, the guy who searched, ip, type of search
        #might required in future for showing captcha or banning
        return render_to_response('home.html',{'errors':errors})


