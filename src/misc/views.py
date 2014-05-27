from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.template.response import TemplateResponse

class Home(View):

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'home.html')

