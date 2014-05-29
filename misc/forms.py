# -*- coding: utf-8 -*-
from django import forms
from models import Migrant 

class MigrantForm(forms.ModelForm):

    class Meta:
        model  = Migrant
        fields = ('pseudo','origin_country','age','gender','dest_country' )
        
        labels = {
            'pseudo': ('Inventa un nombre falso (seudónimo)'),
            'origin_country': ('¿De dónde eres?'),
            'age': ('¿Cuántos años tienes?'),
            'gender': ('¿Cuál es tu género?'),
            'dest_country': ('¿A qué país o ciudad te diriges?'),
        }
