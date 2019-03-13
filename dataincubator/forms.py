from django import forms
from .models import Image
#from django.forms.widgets import FileInput


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('img',)
    

