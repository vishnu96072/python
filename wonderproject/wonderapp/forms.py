from django import forms
from . models import Wonder
class WonderForm(forms.ModelForm):
    class Meta:
        model=Wonder
        fields=['name','desc','img']