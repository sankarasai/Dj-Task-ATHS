from django.forms import ModelForm,widgets
from .models import Ticket
from django import forms

class ticketForm(ModelForm):
    
    class Meta:
        model = Ticket
        fields = ['ticket_name','ticket_description',]
        
        widgets={
            'ticket_name':forms.TextInput(attrs={'class':'form-control'}),
            'ticket_description':forms.Textarea(attrs={'class':'form-control'}),
        }
        
class AdminForm(ModelForm):
    
    class Meta:
        model = Ticket
        fields = ['ticket_name','ticket_description','status']
        
        widgets={
            'ticket_name':forms.TextInput(attrs={'class':'form-control'}),
            'ticket_description':forms.Textarea(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-select'}),
        }
        
