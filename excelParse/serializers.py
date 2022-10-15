
from excelParse.models import MongoDocumentReports
from rest_framework_mongoengine.serializers import DocumentSerializer

class MongoDocumentReportsSerializer(DocumentSerializer):
    class Meta:
        model = MongoDocumentReports
        fields = '__all__'