from rest_framework import serializers
from .models import Dog
#tell django to convert sql to json
class DogSerializer(serializers.ModelSerializer):
    class Meta:
        #tell django which model to use
        model = Dog
        
        #tell django which fields to include
        fiels = ('name', 'breed', 'age', 'gender', 'color', 'image_url', 'weight')