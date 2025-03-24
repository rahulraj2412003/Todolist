from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Landing page
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('complete-task/<int:task_id>/', views.complete_task, name='complete_task'),
]
