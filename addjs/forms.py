from django import forms
from profiles.models import Country, City
from load.models import NewCity


class CountryForm(forms.ModelForm):
    class Meta:
        model = NewCity
        fields = ('country',)
    city = forms.CharField(widget=forms.Select,required=True)
