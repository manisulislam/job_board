from django.contrib.auth.forms import UserCreationForm
from .models import UserProfileInfo
from django.contrib.auth.models import User
from django import forms
USER_TYPES=(
    ("EMPLOYER","EMPLOYER"),
    ("JOBSEEKER","JOBSEEKER")
)
class UserRegisterForm(UserCreationForm):
    user_type=forms.ChoiceField(choices=USER_TYPES)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','user_type']
        