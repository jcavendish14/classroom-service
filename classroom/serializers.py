from rest_framework import serializers
from .models import Students

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ("first_name", "last_name")