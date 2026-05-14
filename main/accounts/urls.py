from django.urls import path ,include
from .views import *
from django.contrib.auth.views import LoginView,PasswordChangeView

urlpatterns=[
    path('',include('projects.urls')),
    path('logout/',logout_view, name="logout"),
    path('signup/',signup_view,name='signup'),
    path('change_password/',PasswordChangeView.as_view(template_name='accounts/change_password.html'),name='change_password'),
    path('login/',LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('edit_my_profile/',edit_profile,name='edit_profile'),
    path('my_profile/',my_profile,name='my_profile'),
]