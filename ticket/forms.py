from django import forms
from .models import Ticket
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class AddTicketForm(forms.ModelForm):
    """Form for add ticket"""
    class Meta:
        model = Ticket
        fields = ('category','title', 'text')
        widgets = {
            'text' : SummernoteWidget(),
            #'text' : SummernoteInplaceWidget()
        }
