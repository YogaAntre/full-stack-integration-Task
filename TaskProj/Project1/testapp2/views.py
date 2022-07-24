from django.shortcuts import render
from .serializers import TaskSerializer
from rest_framework import viewsets
from .models import Task1
# Create your views here.
class TaskDetails(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task1.objects.all()