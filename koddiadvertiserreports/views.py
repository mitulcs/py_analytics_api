from http import HTTPStatus
import json
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets, status
# from rest_framework_mongoengine import viewsets
from koddiadvertiserreports.models import KddiAdvertiserReports
from koddiadvertiserreports.serializers import KddiAdvertiserMediaChannelSerializer, KddiAdvertiserReportsSerializer
# Create your views here.
from rest_framework.views import APIView
from py_analytics_api.custompage import CustomPagination
from collections import OrderedDict
from py_analytics_api.ticks import convert_dotnet_tick, date_to_dotnet_tick
from datetime import datetime
from itertools import groupby
import calendar
from py_analytics_api.utils import getMonthEndDate, getYearEndDate
from py_analytics_api.enums import EnumPaidMediaScreenType, EnumDurationType


class KddiAdvertiserReportsViewSet(viewsets.ViewSet, CustomPagination):
    model = KddiAdvertiserReports
    serializer_class = KddiAdvertiserReportsSerializer

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
        ]), status=status.HTTP_200_OK)

    # def get_queryset(self):
    #     return KddiAdvertiserReports.objects.all()


class KddiAdvertiserMediaChannelViewSet(viewsets.ViewSet):
    model = KddiAdvertiserReports
    serializer_class = KddiAdvertiserMediaChannelSerializer

    def list(self, request):
        properties = request.query_params['properties']
        startDate = request.query_params['startDate']
        endDate = request.query_params['endDate']
        type = request.query_params.get('type')
        durationType = request.query_params.get('durationType')
        mediaChannel = ['Google Hotel Ads', 'TripAdvisor', 'Kayak', 'Trivago']

        listOfProperties = [int(item)
                            for item in properties.split(',') if item.isdigit()]

        if int(durationType) == EnumDurationType.MOM.value:
            firstMonthStartDate = datetime.strptime(startDate, "%Y-%m-%d")
            firstMonthEndDate = getMonthEndDate(
                datetime.strptime(startDate, "%Y-%m-%d"))

            secondMonthStartDate = datetime.strptime(endDate, "%Y-%m-%d")
            secondMonthEndDate = getMonthEndDate(secondMonthStartDate)

            queryset = KddiAdvertiserReports.objects(__raw__={'$and': [{'$or': [{'ReportDate': {'$elemMatch': {'$gte': date_to_dotnet_tick(firstMonthStartDate), '$lte': date_to_dotnet_tick(firstMonthEndDate)}}}, {'ReportDate': {'$elemMatch': {
                                                     '$gte': date_to_dotnet_tick(secondMonthStartDate), '$lte': date_to_dotnet_tick(secondMonthEndDate)}}}]}, {'PropertyId': {'$in': listOfProperties}}, {'MediaChannel': {'$in': mediaChannel}}]})
        elif int(durationType) == EnumDurationType.YOY.value:
            firstYearStartDate = datetime.strptime(startDate, "%Y-%m-%d")
            firstYearEndDate = getYearEndDate(
                datetime.strptime(startDate, "%Y-%m-%d"))

            secondYearStartDate = datetime.strptime(endDate, "%Y-%m-%d")
            secondYearEndDate = getYearEndDate(secondYearStartDate)

            queryset = KddiAdvertiserReports.objects(__raw__={'$and': [{'$or': [{'ReportDate': {'$elemMatch': {'$gte': date_to_dotnet_tick(firstYearStartDate), '$lte': date_to_dotnet_tick(firstYearEndDate)}}}, {'ReportDate': {'$elemMatch': {
                                                     '$gte': date_to_dotnet_tick(secondYearStartDate), '$lte': date_to_dotnet_tick(secondYearEndDate)}}}]}, {'PropertyId': {'$in': listOfProperties}}, {'MediaChannel': {'$in': mediaChannel}}]})
        else:
            queryset = KddiAdvertiserReports.objects(__raw__={"$and": [{"ReportDate": {"$elemMatch": {"$gte": date_to_dotnet_tick(
                startDate), "$lte": date_to_dotnet_tick(endDate)}}}, {"PropertyId": {"$in": listOfProperties}}, {"MediaChannel": {"$in": mediaChannel}}]})

        serializer = KddiAdvertiserMediaChannelSerializer(queryset, many=True)
        json_object = json.loads(json.dumps(serializer.data))

        json_object.sort(key=lambda content: content['propertyId'])
        propertyGroups = groupby(
            json_object, lambda content: content['propertyId'])

        if int(type) == EnumPaidMediaScreenType.MetaSearchDashboard.value:
            listData = []
            for propertyId, propertyData in propertyGroups:
                values = list(propertyData)
                mapData = dict()
                revenue = sum(float(c['revenue']) for c in values)
                spend = sum(float(d['spend']) for d in values)
                clicks = sum(float(d['clicks']) for d in values)
                bookings = sum(float(d['bookings']) for d in values)
                mapData['propertyId'] = propertyId
                mapData['revenue'] = revenue
                mapData['spend'] = spend
                mapData['clicks'] = clicks
                mapData['bookings'] = bookings
                listData.append(mapData)
        else:
            listData = []
            for propertyId, propertyData in propertyGroups:
                prop = list(propertyData)
                mapData = dict()
                mapData['propertyId'] = propertyId
                mapData['data'] = getDataByMediaChannel(prop, mediaChannel)
                listData.append(mapData)

        return Response(OrderedDict([
            ('results', listData)
        ]), status=status.HTTP_200_OK)


def getDataByMediaChannel(prop, mediaChannel):
    listData = []
    for value in mediaChannel:
        reportMap = dict()
        reportMap['mediaChannel'] = value
        listMediaChannelData = filter(
            lambda element:
            element['mediaChannel'] == value, prop)
        reportMap['channelData'] = list(listMediaChannelData)
        listData.append(reportMap)
    return listData
    # prop.sort(key=lambda content: content['mediaChannel'])
    # reportDateGroups = groupby(
    #     prop, lambda content: content['mediaChannel'])
    # listData = []
    # for reportDate, v in reportDateGroups:
    #     reportMap = dict()
    #     val = list(v)
    #     reportMap['mediaChannel'] = reportDate
    #     reportMap['channelData'] = val
    #     listData.append(reportMap)
    # return listData
