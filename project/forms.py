from django.forms import ModelForm,widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','feature_image','description','demo_link','tags','source_link']
        widgets ={
            'tags': forms.CheckboxSelectMultiple(),
        }