from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import transaction
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View
from django.template.response import TemplateResponse
from models import Migrant, CheckPoint



class DisplayPath(View):
    def post(self, request, *args, **kwargs):
        pseudo_name =  request.POST.get('searchname',None) 
        errors = []
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
            return render_to_response('display_migrant_location.html',{'migrant':migrant,'checkpoints':checkpoints,'errors':errors})
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

