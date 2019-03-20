from django import forms


class LoadFile(forms.Form):
    file = forms.FileField(allow_empty_file=False)
