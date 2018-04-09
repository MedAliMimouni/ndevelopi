from django.shortcuts import render
from .forms import MessageForm,ProjectForm
# Create your views here.


def contact(resuest):
    message_form = MessageForm()
    project_form = ProjectForm()
    return render(resuest,'contact/contact.html',{'message_form':message_form,'project_form':project_form})