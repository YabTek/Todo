from rest_framework import viewsets
from .models import Task, User, Checklist
from .serializers import TaskSerializer, UserSerializer, ChecklistSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    
   