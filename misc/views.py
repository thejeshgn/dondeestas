from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import transaction
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.generic import View
from django.template.response import TemplateResponse
from models import Migrant, CheckPoint
from misc.forms import MigrantForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json
import requests
import logging

logger = logging.getLogger(__name__)

class DisplayPath(View):
    def post(self, request, *args, **kwargs):
        pseudo_name =  request.POST.get('searchname',None) 
        errors = []
        migrant = None
        if pseudo_name:
            try:
                migrant = Migrant.objects.get(pseudo=pseudo_name)
            except Migrant.DoesNotExist:
                #error, just say migrant doesnt exist
                errors.append('Pseudo name not found. Please enter a valid one.')
                #log, the guy who searched, ip, pseudo name, type of search
                #might required in future for showing captcha or banning
                return redirect('/', errors=errors)

            #future path of the migrant
            checkpoints = CheckPoint.objects.filter(migrante=migrant)
            point = []
            point.append(float(migrant.origin_lng))
            point.append(float(migrant.origin_lat))
            multiLineArray = []
            for i in range(0,len(checkpoints)):
                lineArray = []
                #starting point
                if i ==0:
                    lineArray.append(point)  
                else:
                    checkpoint = checkpoints[i-1]
                    point = []
                    point.append(float(checkpoint.lon))
                    point.append(float(checkpoint.lat))
                    lineArray.append(point)

                #endpoint
                checkpoint = checkpoints[i]
                point = []
                point.append(float(checkpoint.lon))
                point.append(float(checkpoint.lat))
                lineArray.append(point)
                multiLineArray.append(lineArray)


            path_covered = json.dumps(multiLineArray)


            #future path of the migrant
            lineArray = []
            no_of_checkpoints = len(checkpoints)
            if checkpoints and no_of_checkpoints > 0: 
                last_checkpoint = checkpoints[no_of_checkpoints-1]
                point = []
                point.append(float(last_checkpoint.lon))
                point.append(float(last_checkpoint.lat))
                lineArray.append(point)
            else:
                point = []
                point.append(float(migrant.origin_lng))
                point.append(float(migrant.origin_lat))
                lineArray.append(point)  

            point = []
            point.append(float(migrant.dest_lng))
            point.append(float(migrant.dest_lat))
            lineArray.append(point)  

            future_path= json.dumps(lineArray)


            return render_to_response('display_migrant_location2.html',{'migrant':migrant,'path_covered':path_covered,'future_path':future_path,'errors':errors})
        else:
            #error: please enter a pseudo name
            errors.append('Please enter a valid Pseudo name')
            #log, the guy who searched, ip, type of search
            #might required in future for showing captcha or banning
            return redirect('/', errors=errors)

    def get(self, request, *args, **kwargs):
        errors = []
        errors.append('Pseudo name not found. Please enter a valid one.')
        return redirect('/',errors=errors)

class Home(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'home.html')

class Register(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'register.html')

def MigrantCreate(request):
    if request.POST:
        form = MigrantForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = MigrantForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('register.html', args)


class CheckPointView(View):
    def post(self, request, *args, **kwargs):
        pseudo_name =  request.POST.get('searchname',None) 
        errors = []
        migrant = None
        if pseudo_name:
            try:
                migrant = Migrant.objects.get(pseudo=pseudo_name)
            except Migrant.DoesNotExist:
                #error, just say migrant doesnt exist
                errors.append('Pseudo name not found. Please enter a valid one.')
                #log, the guy who searched, ip, pseudo name, type of search
                #might required in future for showing captcha or banning
                return redirect('/', errors=errors)
            return render_to_response('checkpoint.html',{'migrant':migrant})
        else:
            #error: please enter a pseudo name
            errors.append('Please enter a valid Pseudo name')
            #log, the guy who searched, ip, type of search
            #might required in future for showing captcha or banning
            return redirect('/', errors=errors)

    def get(self, request, *args, **kwargs):
        errors = []
        errors.append('Pseudo name not found. Please enter a valid one.')
        return redirect('/',errors=errors)

class CheckPointSave(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CheckPointSave, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):        
        pseudo_name =  request.POST.get('pseudo_name',None) 
        latitude =  request.POST.get('latitude',None) 
        longitude =  request.POST.get('longitude',None) 
        print pseudo_name, latitude, longitude
        errors = []
        migrant = None
        if pseudo_name:
            try:
                migrant = Migrant.objects.get(pseudo=pseudo_name)
            except Migrant.DoesNotExist:
                #error, just say migrant doesnt exist
                errors.append('Pseudo name not found. Please enter a valid one.')
                #log, the guy who searched, ip, pseudo name, type of search
                #might required in future for showing captcha or banning
                return redirect('/', errors=errors)

            print "got the name"
            #if valid migrant, and location
            if latitude and longitude:
                url = 'http://api.geonames.org/findNearbyPlaceNameJSON?lng='+longitude+'&lat='+latitude+'&username=thejeshgn'
                data = json.loads(requests.get(url).text)
                country = data['geonames'][0]['countryName']
                name = data['geonames'][0]['name']
                checkpoint = CheckPoint(migrante=migrant,lon=longitude,lat=latitude,other_location='',city=name,state='',country=country)
                checkpoint.save()

                #future path of the migrant for display
                checkpoints = CheckPoint.objects.filter(migrante=migrant)
                point = []
                point.append(float(migrant.origin_lng))
                point.append(float(migrant.origin_lat))
                multiLineArray = []
                for i in range(0,len(checkpoints)):
                    lineArray = []
                    #starting point
                    if i ==0:
                        lineArray.append(point)  
                    else:
                        checkpoint = checkpoints[i-1]
                        point = []
                        point.append(float(checkpoint.lon))
                        point.append(float(checkpoint.lat))
                        lineArray.append(point)

                    #endpoint
                    checkpoint = checkpoints[i]
                    point = []
                    point.append(float(checkpoint.lon))
                    point.append(float(checkpoint.lat))
                    lineArray.append(point)
                    multiLineArray.append(lineArray)


                path_covered = json.dumps(multiLineArray)


                #future path of the migrant
                lineArray = []
                no_of_checkpoints = len(checkpoints)
                if checkpoints and no_of_checkpoints > 0: 
                    last_checkpoint = checkpoints[no_of_checkpoints-1]
                    point = []
                    point.append(float(last_checkpoint.lon))
                    point.append(float(last_checkpoint.lat))
                    lineArray.append(point)
                else:
                    point = []
                    point.append(float(migrant.origin_lng))
                    point.append(float(migrant.origin_lat))
                    lineArray.append(point)  

                point = []
                point.append(float(migrant.dest_lng))
                point.append(float(migrant.dest_lat))
                lineArray.append(point)  
                future_path= json.dumps(lineArray)
                return render_to_response('display_migrant_inbox.html',{'migrant':migrant,'path_covered':path_covered,'future_path':future_path,'errors':errors})


        else:
            #error: please enter a pseudo name
            errors.append('Please enter a valid Pseudo name')
            #log, the guy who searched, ip, type of search
            #might required in future for showing captcha or banning
            return redirect('/', errors=errors)




    def get(self, request, *args, **kwargs):
        errors = []
        errors.append('Pseudo name not found. Please enter a valid one.')
        return redirect('/',errors=errors)
