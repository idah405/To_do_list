from .models import *
from django import forms
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = task

        fields = fields = ['name', 'description', 'completed']