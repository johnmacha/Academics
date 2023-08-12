from django import forms
from django.forms import ModelForm
from .models import Teacher

class TeachersForm(ModelForm):
   class Meta:
    model = Teacher
    fields = '__all__'
