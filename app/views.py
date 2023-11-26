from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def employeedata(request):
    empdata=employee.objects.all()
    empjsondata=employeemodelserializers(empdata,many=True)
    return Response(empjsondata.data)
