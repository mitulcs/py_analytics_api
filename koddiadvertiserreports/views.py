from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework_mongoengine import viewsets
from koddiadvertiserreports.models import KddiAdvertiserReports
from koddiadvertiserreports.serializers import KddiAdvertiserReportsSerializer
# Create your views here.
from rest_framework.views import APIView
from py_analytics_api.custompage import CustomPagination
from collections import OrderedDict


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
        listOfProperties = [int(item)
                            for item in properties.split(',') if item.isdigit()]
        # propertyId__in=listOfProperties,
# {ReportDate: { $elemMatch: { $gte: 636503616000000000, $lte: 636525216000000000}}}
        # queryset = KddiAdvertiserReports.objects.filter( reportDate__match={'reportDate__gte': '636503616000000000', 'reportDate__lte': 636525216000000000}
        #     )
        queryset = KddiAdvertiserReports.objects.filter(propertyId__in=listOfProperties)
# reportDate__gte=636503616000000000, reportDate__lte=636525216000000000
        page = self.paginate_queryset(queryset, request)
        if page is not None:
            serializer = KddiAdvertiserReportsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = KddiAdvertiserReportsSerializer(queryset, many=True)
        # print(serializer.data)
        return Response(OrderedDict([
            ('count', len(serializer.data)),
            ('next', None),
            ('previous', None),
            ('results', serializer.data)
        ]))

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
