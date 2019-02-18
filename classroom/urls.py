from django.urls import path
from .views import ListStudentsView

urlpatterns = [
    path('students/', ListStudentsView.as_view(), name="students-all")
]