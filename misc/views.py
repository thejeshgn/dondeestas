from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import transaction
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View
from django.template.response import TemplateResponse
from models import Migrant, CheckPoint
import json


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

            checkpoints = CheckPoint.objects.filter(migrante=migrant)
            lineArray = []
            point = []
            point.append(float(migrant.origin_lng))
            point.append(float(migrant.origin_lat))
            lineArray.append(point)  
            for checkpoint in checkpoints:
                point = []
                point.append(float(checkpoint.lon))
                point.append(float(checkpoint.lat))
                lineArray.append(point)
            path_covered = json.dumps(lineArray)


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


            return render_to_response('display_migrant_location.html',{'migrant':migrant,'path_covered':path_covered,'future_path':future_path,'errors':errors})
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

