from django.urls import path,include
from .views import *

urlpatterns=[
    path('', include('projects.url_form')),
    path('projects/', all_projects,name='all_projects'),
    path('projects/<int:project_id>/', groups, name="groups"),
    path('projects/<int:project_id>/group/<int:group_id>/',members,name='member_group'),
    path('projects/<int:project_id>/group/<int:group_id>/member_tasks/<int:user_id>',all_tasks,name='tasks'),
    path('projects/<int:project_id>/group/<int:group_id>/member/task/<int:user_id>',task,name='task'),
    path('show_profile/<int:profile_id>',show_profile,name='show_profile')
]