from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet, ChecklistViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')  
router.register(r'checklists', ChecklistViewSet, basename='checklist')  

urlpatterns = [
    path('', include(router.urls)),
]
