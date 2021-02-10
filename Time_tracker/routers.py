# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from tracker.viewsets import *

router = routers.DefaultRouter()

# router.register('WorkHours', WorkHourViewSet)
