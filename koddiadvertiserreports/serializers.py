
from rest_framework_mongoengine.serializers import DocumentSerializer
from koddiadvertiserreports.models import KddiAdvertiserReports
from py_analytics_api.ticks import convert_dotnet_tick
from datetime import datetime

class KddiAdvertiserReportsSerializer(DocumentSerializer):
    class Meta:
        model = KddiAdvertiserReports
        fields = '__all__'

    def to_representation(self, instance):
        data = super(DocumentSerializer, self).to_representation(instance)
        data['spend'] = float(data['spend'])
        data['revenue'] = float(data['revenue'])
        if (isinstance(data.get('modifiedOn'), list)):
            data['modifiedOn'] = convert_dotnet_tick(
                int(data.get('modifiedOn')[0]))
        if (isinstance(data.get('createdOn'), list)):
            data['createdOn'] = convert_dotnet_tick(
                int(data.get('createdOn')[0]))
        if (isinstance(data.get('reportDate'), list)):
            tickDate = convert_dotnet_tick(
                int(data.get('reportDate')[0]))
            date_time_obj = datetime.strptime(tickDate, "%Y-%m-%dT%H:%M:%S.%f")
            data['reportDate'] = date_time_obj.strftime("%Y-%m")
        return data
