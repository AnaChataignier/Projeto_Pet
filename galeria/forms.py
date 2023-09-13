from django import forms

from galeria.models import Pet

class PetForms(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['publicada',]
        labels = {
            'descricao':'Descrição',
            'data_cadastro': 'Data de registro',
            'tutor': 'Tutor',
            'categoria': 'Categoria',
            'nome': 'Nome',
            'idade':'Idade',
            'cor':'Cor',
            'foto':'Foto',
            'raca':'Raça',
            
        }
    
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'raca': forms.TextInput(attrs={'class':'form-control'}),
            'cor': forms.TextInput(attrs={'class':'form-control'}),
            'idade': forms.NumberInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_cadastro': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'tutor': forms.Select(attrs={'class':'form-control'}),
        } 