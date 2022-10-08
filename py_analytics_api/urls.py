"""mongoAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_mongoengine import mongo_admin, mongo_auth
from rest_framework.routers import DefaultRouter
from employee.views import KoddiApiView, KoddiFilesViewSet
from users.views import UserViewSet, CreateSuperUserAPIView
# from users.views import *
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
# router.register(r'employee', EmployeeViewSet, basename='user')
router.register(r'koddiFiles', KoddiFilesViewSet, basename='koddiFilesViewSet')
# router.register(r'create_superuser', CreateSuperUserAPIView.as_view(), basename='create_superusers')
# router.add_api_view(r'create_superuser', url(r'^create_superuser/$', CreateSuperUserAPIView.as_view(), name=r"create_superusers"))

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('users/', views.article_detail),
    path('api/', include(router.urls)),
    path('create_superuser/', CreateSuperUserAPIView.as_view(), name="create_superuser"),
    path('koddiFiles/', KoddiApiView.as_view()),
    # path('mongoauth', mongo_auth)
    # path('admin/', mongo_admin.site.urls),
]
