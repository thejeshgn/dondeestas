# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Transgender','Transgender'),    
    ('Unknown','Unknown'),        
    )

MARTIAL_STATUS=(
    ('Married','Married'),
    ('Single','Single'),
    ('Divorced','Divorced'),    
    ('Unknown','Unknown'),        
    )

ABUSE_TYPES =(
    ('A01','Me extorsionaron las autoridades'),
    ('A02','Me robaron los maquinistas del tren'),
    ('A03','Me obligaron a transportar droga'),
    ('A04','Le pagué a un “pollero” o “guía” para que me llevara a mi destino'),
    ('A05','Vi como traficaban con órganos'),
    ('A06','Me torturaron'),
    ('A07','Vi asesinatos'),
    ('A08','Me secuestraron'),
    ('A09','Me usaron de esclavo (trata de personas)'),
    ('A10','Me violaron'),
    ('Others', 'Otro')      
    )


# Create your models here.
class Migrant(models.Model):
    def __unicode__(self):
        return u'%s:%s:%s' % (self.id, self.pseudo, self.origin_country)

    pseudo          = models.CharField(max_length=200, unique=True)
    origin_country = models.CharField(max_length=50, blank=True,null=True)
    #origin defaults to Mexico
    origin_lat      = models.CharField(max_length=20, blank=True,null=True,default='18.222829375236')
    origin_lng      = models.CharField(max_length=20, blank=True,null=True,default='-99.0904998779297')
    age             = models.IntegerField(default=0)
    gender          = models.CharField(max_length=15,choices=GENDER,default='Unknown')
    dest_country    = models.CharField(max_length=50, blank=True,null=True)
    #destination defaults to LA, USA
    dest_lat        = models.CharField(max_length=20, blank=True,null=True,default='34.052235')
    dest_lng        = models.CharField(max_length=20, blank=True,null=True,default='-118.243683')
    martial         = models.CharField(max_length=15,choices=MARTIAL_STATUS,default='Unknown')
    created         = models.DateTimeField(default=datetime.now)
    updated         = models.DateTimeField(default=datetime.now)


class Abuse(models.Model):
    type            = models.CharField(max_length=100,choices=ABUSE_TYPES,default='Others')
    description     = models.CharField(max_length=2000)
    migrante        = models.ForeignKey(Migrant)
    created         = models.DateTimeField(default=datetime.now)


class CheckPoint(models.Model):
    def __unicode__(self):
        return u'%s:%s:%s' % (self.id, self.migrante.pseudo, self.city)

    migrante        = models.ForeignKey(Migrant)    
    lon             = models.CharField(max_length=20, blank=True,null=True)
    lat             = models.CharField(max_length=20, blank=True,null=True)
    other_location  = models.CharField(max_length=100, blank=True,null=True)
    city            = models.CharField(max_length=100)
    state           = models.CharField(max_length=100)
    country         = models.CharField(max_length=100)
    created         = models.DateTimeField(default=datetime.now)
