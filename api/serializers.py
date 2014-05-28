from django.contrib.auth.models import User, Group
from misc.models import Migrant, Abuse, CheckPoint
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MigrantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Migrant
        fields = ('pseudo','origin_country','age','gender','dest_country','martial','created','updated')

class AbuseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Abuse
        fields = ('type','description','migrante','created')


class CheckPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckPoint
        fields = ('migrante','lon','lat','other_location','city','state','country','created')

