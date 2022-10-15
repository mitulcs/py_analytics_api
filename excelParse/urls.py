
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from excelParse.views import ExcelParseViewSet
from excelParse import views
# from users.views import *
router = DefaultRouter()
router.register(r'excelParse',
                ExcelParseViewSet, basename='excelParse')

urlpatterns = [
    path('excel/', include(router.urls)),
]
