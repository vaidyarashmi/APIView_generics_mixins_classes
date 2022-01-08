from django.core.exceptions import ValidationError
from rest_framework import serializers
from testapp.models import Employee

class EmployeeSerializers(serializers.ModelSerializer):        
    class Meta:
        model=Employee
        fields='__all__'
