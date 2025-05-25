from django import forms
from .models import Application

class Form(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'resume': forms.FileInput(attrs={'accept': '.pdf, .doc, .docx'}),
            }