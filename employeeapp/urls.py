from django.urls import path
from employeeapp import views
from employeeapp.models import Departments


urlpatterns=[
    path('department/',views.departmentApi, name='department'),
    path('employee/' ,views.departmentApi, name='employee')

]