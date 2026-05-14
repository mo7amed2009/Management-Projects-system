from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'
    

class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields='__all__'



class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'