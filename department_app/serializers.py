from rest_framework import serializers

from department_app.models import Department

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')

    def create(self,data):
        instance = Department.objects.create(**data)
        return instance 
