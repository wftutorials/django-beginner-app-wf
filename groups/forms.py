from django.forms import ModelForm
from .models import Groups, Members
from django.contrib.auth.models import User

class GroupForm(ModelForm):
    class Meta:
        model = Groups
        exclude = ('created_at', )

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')

class MemberForm(ModelForm):
    class Meta:
        model = Members
        exclude = ('created_at', )