
from django.forms import ModelForm
from .models import Portal

class AddPortal(ModelForm):
    class Meta:
        model = Portal
        fields = '__all__'