from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from koddiadvertiserreports.views import KddiAdvertiserReportsViewSet

# from users.views import *
router = DefaultRouter()
router.register(r'kddiAdvertiserReports',
                KddiAdvertiserReportsViewSet, basename='KddiAdvertiserReports')
# router.register(r'kapi/',
#                 ProductAPIView.as_view(), basename='KddiAdvertiserReports')

urlpatterns = [
   path('', include(router.urls)),
#    path('kapi/', ProductAPIView.as_view(),  name="kapia")
]