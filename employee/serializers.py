from rest_framework_mongoengine.serializers import DocumentSerializer
from employee.models import Employee, KoddiFiles

class EmployeeSerializer(DocumentSerializer):
    class Meta:
        model = Employee
        fields = '__all__'



class KoddiFilesSerializer(DocumentSerializer):
    class Meta:
        model = KoddiFiles
        fields = '__all__'