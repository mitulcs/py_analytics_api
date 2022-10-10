from rest_framework.response import Response
from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from koddiadvertiserreports.models import KddiAdvertiserReports
from koddiadvertiserreports.serializers import KddiAdvertiserReportsSerializer
# Create your views here.
from rest_framework.views import APIView
from py_analytics_api.custompage import CustomPagination


class KddiAdvertiserReportsViewSet(viewsets.ModelViewSet):
    """
    Read-only User endpoint
    """
    # permission_classes = (permissions.IsAuthenticated, )  # IsAdminUser?
    # authentication_classes = (TokenAuthentication, )
    model = KddiAdvertiserReports
    serializer_class = KddiAdvertiserReportsSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return KddiAdvertiserReports.objects.all()
        # size = self.request.GET.get('size')
        # if (int(size) == 0):
        #     return Response({"results": KddiAdvertiserReports.objects.all()})
        # return KddiAdvertiserReports.objects.all()
