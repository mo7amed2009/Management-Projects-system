from django.urls import path
from .views import *

urlpatterns=[
    path('add_project/',add_project,name='add_project'),
    path('add_group/',add_group,name='add_group'),
    path('add_task/',add_task,name='add_task'),
    path('update_project/<int:project_id>/',update_project,name='update_project'),
    path('update_group/project/<int:project_id>/group/<int:group_id>',update_group,name='update_group'),
    path('update_task/project/<int:project_id>/group/<int:group_id>/task/<int:task_id>',update_task,name='update_task'),
]