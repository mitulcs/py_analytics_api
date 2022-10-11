
from rest_framework_mongoengine.serializers import DocumentSerializer
from koddiadvertiserreports.models import KddiAdvertiserReports

class KddiAdvertiserReportsSerializer(DocumentSerializer):
    class Meta:
        model = KddiAdvertiserReports
        fields = '__all__'

    # def to_representation(self, instance):
    #     data = super(DocumentSerializer, self).to_representation(instance)

    #     result = {}
    #     result = data
    #     # result['modifiedOn'] = data['modifiedOn']
    #     # result['version'] = '1.0'
    #     # result['statusCode'] = '2xx'
    #     return data