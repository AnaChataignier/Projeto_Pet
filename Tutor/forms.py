from typing import Any, Dict
from django import forms 
from Tutor.models import Tutor

class CadastroForms(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = {
            'nome':'Nome Tutor',
            'email':'Email',
            'telefone':'Telefone',
            'endereco':'Endereço'
        }
    
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'telefone': forms.NumberInput(attrs={'class':'form-control'}),
            'endereco':forms.TextInput(attrs={'class':'form-control'}),
            }
    
    
    
       
    
   
            
        
            
        