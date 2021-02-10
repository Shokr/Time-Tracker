from rest_framework import viewsets

from serializers import *


# ViewSets define the view behavior.
class WorkHourViewSet(viewsets.ModelViewSet):
    queryset = WorkHour.objects.all()
    serializer_class = WorkHourSerializer
