from django.http import JsonResponse
from django.shortcuts import render
from requests import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from department_app.models import Department
from department_app.serializers import DepartmentSerializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET', 'POST'])
def Employee(request):
    if request.method == "GET":
        data=request.data
        query= Department.objects.all()
        serializers = DepartmentSerializers(query, many=True)
        return JsonResponse(serializers.data, safe=False)

    elif request.method == "POST":
        dept_query = DepartmentSerializers(data=request.data)
        if dept_query.is_valid():
            dept_query.save()
        return JsonResponse(dept_query.data)
    

