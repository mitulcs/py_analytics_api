from pyexpat import model
from unicodedata import name
from django.shortcuts import render
from rest_framework import views, mixins, permissions, exceptions
from rest_framework_mongoengine import viewsets
from employee.models import Employee, KoddiFiles
from employee.serializers import EmployeeSerializer, KoddiFilesSerializer
from rest_framework.response import Response
from py_analytics_api.settings import client
from bson import json_util
import json


# class EmployeeViewSet(viewsets.ModelViewSet):
#     """
#     Read-only User endpoint
#     """
#     # permission_classes = (permissions.IsAuthenticated, )  # IsAdminUser?
#     # authentication_classes = (TokenAuthentication, )
#     serializer_class = EmployeeSerializer

#     def get_queryset(self):
#         return Employee.objects.all()

class  KoddiFilesViewSet(viewsets.ModelViewSet):
    """
    Read-only User endpoint
    """
    # permission_classes = (permissions.IsAuthenticated, )  # IsAdminUser?
    # authentication_classes = (TokenAuthentication, )
    model = KoddiFiles
    serializer_class = KoddiFilesSerializer
   
    def get_queryset(self):
        return  KoddiFiles.objects.all()


class KoddiApiView(views.APIView):

    def get(self, request, format=None):
        # pass
        # collection = client.project.employee
        collection = client.HotalDb20201126.koddifiles
        # data = collection.find({'_id': '62b2d9038f52c6d62b51c2e8'})
        # print('data')
        # print(db.list_collections())
        # print(data)
        list_cur = collection.find()
        json_data = json.loads(json_util.dumps(list_cur, default=json_util.default,))
        # print('Data')
        # print(json_data)
        # for doc in collection.find():
        #   print(doc)

        # for item in list_cur:
        #     print('s')
        #     print(list_cur[item])
        
        return Response({'some': json_data})