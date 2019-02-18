from rest_framework import generics
from .models import Students
from .serializers import StudentsSerializers

class ListStudentsView(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers