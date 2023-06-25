from django.forms import ModelForm, DateInput
from .models import Todo

class TdodForms(ModelForm):
    class Meta:
        model = Todo
        exclude = ('date',)
        widgets = {
            'estimad_end' : DateInput(attrs={'type': 'date'}),
        }

    