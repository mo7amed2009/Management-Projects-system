from django import forms
from .models import User, Profile


class UserForm (forms.ModelForm):
    class Meta:
        model=User
        fields =[
            'email',
            'username',
            'password',
            # 'is_manger',
            # 'is_senior',
            # 'is_junior',
            
           
        ]
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'