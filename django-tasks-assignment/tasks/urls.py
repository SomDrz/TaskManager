from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.taskCreate, name='task-list-create'), #create and filter
    path('tasks/<int:pk>/', views.taskUpdate, name='task-update'),  # patch
    path('tasks/<int:pk>/delete/', views.taskDelete, name='task-delete'),  # DELETE
]
