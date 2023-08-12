from django.forms import ModelForm
from .models import Marks

class ResultsForm(ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'