from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from koddiadvertiserreports.views import KddiAdvertiserReportsViewSet, KddiAdvertiserMediaChannelViewSet

router = DefaultRouter()
router.register(r'kddiAdvertiserReports',
                KddiAdvertiserReportsViewSet, basename='KddiAdvertiserReports')
router.register(r'koddiMediaChannel',
                KddiAdvertiserMediaChannelViewSet, basename='koddiMediachannels')

urlpatterns = [
    path('', include(router.urls)),
]
