from .models import Message,Project
from django.forms import ModelForm

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['email','subject']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name','tel_number','email','idea']
