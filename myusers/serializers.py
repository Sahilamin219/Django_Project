from rest_framework import serializers
from .models import Profile, Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Hero
        fields = ('id', 'image' , 'user', )
        # fields = ('name', 'alias')
# serialization is the process of converting a Model to JSON.
# Using a serializer, we can specify what fields should be present
# in the JSON representation of the model.