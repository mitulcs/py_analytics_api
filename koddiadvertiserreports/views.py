from http import HTTPStatus
import json
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets, status
# from rest_framework_mongoengine import viewsets
from koddiadvertiserreports.models import KddiAdvertiserReports, KddiAdvertiserReportsResponseElement
from koddiadvertiserreports.serializers import KddiAdvertiserReportsSerializer
# Create your views here.
from rest_framework.views import APIView
from py_analytics_api.custompage import CustomPagination
from collections import OrderedDict
from py_analytics_api.ticks import convert_dotnet_tick, date_to_dotnet_tick
from datetime import datetime
from itertools import groupby


class KddiAdvertiserReportsViewSet(viewsets.ViewSet, CustomPagination):
    """
    Read-only User endpoint
    """
    # permission_classes = (permissions.IsAuthenticated, )  # IsAdminUser?
    # authentication_classes = (TokenAuthentication, )
    model = KddiAdvertiserReports
    serializer_class = KddiAdvertiserReportsSerializer
    # pagination_class = CustomPagination

    def list(self, request):
        properties = request.query_params['properties']
        startDate = request.query_params['startDate']
        endDate = request.query_params['endDate']
        properties = request.query_params['properties']
        listOfProperties = [int(item)
                            for item in properties.split(',') if item.isdigit()]

        # print('StartDate:', date_to_dotnet_tick(startDate),
        #       'EndDate:', date_to_dotnet_tick(endDate))

        queryset = KddiAdvertiserReports.objects(__raw__={"$and": [{"ReportDate": {"$elemMatch": {"$gte": date_to_dotnet_tick(
            startDate), "$lte": date_to_dotnet_tick(endDate)}}}, {"PropertyId": {"$in": listOfProperties}}]})

        page = self.paginate_queryset(queryset, request)
        if page is not None:
            serializer = KddiAdvertiserReportsSerializer(page, many=True)
            json_object = json.loads(json.dumps(serializer.data))
            return self.get_paginated_response(json_object)

        serializer = KddiAdvertiserReportsSerializer(queryset, many=True)
        json_object = json.loads(json.dumps(serializer.data))

        json_object.sort(key=lambda content: content['reportDate'])
        groups = groupby(json_object, lambda content: content['reportDate'])
        
        listData = []
        for reportDate, group in groups:
            values = list(group)
            revenue = sum(c['revenue'] for c in values)
            spend = sum(float(d['spend']) for d in values)
            mapData = dict()
            mapData['reportDate'] = reportDate
            mapData['revenue'] = revenue
            mapData['spend'] = spend
            listData.append(mapData)

        return Response(OrderedDict([
            ('results', listData)
        ]), status= status.HTTP_200_OK)

    # def get_queryset(self):
    #     return KddiAdvertiserReports.objects.all()


# class KddiAdvertiserReportsViewSet(viewsets.ViewSet):
#     """
#     Read-only User endpoint
#     """
#     # permission_classes = (permissions.IsAuthenticated, )  # IsAdminUser?
#     # authentication_classes = (TokenAuthentication, )
#     model = KddiAdvertiserReports
#     serializer_class = KddiAdvertiserReportsSerializer
#     pagination_class = CustomPagination

#     def list(self, request):
#         queryset = KddiAdvertiserReports.objects.all()
#         serializer = KddiAdvertiserReportsSerializer(queryset, many=True)
#         return Response(serializer.data)
