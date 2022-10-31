from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('sensor', views.SensorViewSet, 'sensor')

urlpatterns = router.urls