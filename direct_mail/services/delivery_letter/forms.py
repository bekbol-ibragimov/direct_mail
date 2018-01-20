from django import forms

from .models import Letter


class LetterForm(forms.Form):
    file = forms.FileField()
