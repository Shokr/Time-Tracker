from rest_framework import serializers
from .models import *


# Serializers define the API representation.
class WorkHourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkHour
        fields = ["__all__"]
