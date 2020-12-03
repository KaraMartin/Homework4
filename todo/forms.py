from django import forms
from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    # completed = forms.BooleanField(label='Completed')
    # ,widget=forms.CheckboxInput(attrs={'class': "fas fa-check-square fa-3x",})
