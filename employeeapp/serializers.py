from rest_framework import serializers
from employeeapp.models import Departments,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('Departmentid','DepartmentName')    

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('Employeeid','Employeename','Department','DateOfJoining','PhotoFileName')        