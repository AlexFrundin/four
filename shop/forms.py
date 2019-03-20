from django import forms
from .models import Edit


class MyForm(forms.Form):
    q = forms.IntegerField()
    list_name = forms.CharField(max_length=100)
    category_name = forms.CharField(max_length=100)

class MyFormModels(forms.ModelForm):
    class Meta:
        model = Edit
        fields = '__all__'
