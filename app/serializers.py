from rest_framework import serializers
from app.models import *
class employeemodelserializers(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'