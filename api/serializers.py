from rest_framework import serializers
from .models import Checklist, Task
 
class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    checklists = ChecklistSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'