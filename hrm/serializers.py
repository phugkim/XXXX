### Model ###
from .models import Person
from django.contrib.auth.models import User, Group
### Rest framework ###
from rest_framework import serializers


class GetAllPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','name', 'description', 'phone_number', 'is_live', 'amount']
         #name, description, phone_number, is_live, amount, extra_name, create_at, update_at

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']