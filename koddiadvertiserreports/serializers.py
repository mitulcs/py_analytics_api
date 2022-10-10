
from rest_framework_mongoengine.serializers import DocumentSerializer
from koddiadvertiserreports.models import KddiAdvertiserReports

class KddiAdvertiserReportsSerializer(DocumentSerializer):
    class Meta:
        model = KddiAdvertiserReports
        fields = '__all__'