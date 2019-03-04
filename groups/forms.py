from django.forms import ModelForm
from .models import Groups

class GroupForm(ModelForm):
    class Meta:
        model = Groups
        exclude = ('created_at', )
