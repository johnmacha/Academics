from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length = 20, required = True, help_text = 'Required')
    last_name = forms.CharField(max_length = 20,required = True, help_text='Required')
    email = forms.EmailField(required = True)
    student_id = forms.CharField(max_length = 20, required = True, help_text = 'Required')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email','student_id', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit = True):
        user = super(SignupForm, self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name'] 
        user.save()
        user.email = self.cleaned_data['email']
        user.student_id = self.cleaned_data['student_id']
        return user