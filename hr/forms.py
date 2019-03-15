from django import forms
from .models import *




class Technology_typeForm(forms.ModelForm):
    class Meta:
        model = Technology_type
        fields = ('name',)
