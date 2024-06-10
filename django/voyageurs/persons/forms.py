from django import forms
import re

from persons.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["nom", "date_naissance", "numero_cni", "numero_passeport", "mouvement", "provenance_destination", "date_mouvement", "frontiere"]

        labels = {
            "nom" : "Nom complet du voyageur:",
            "date_naissance" : "Date de naissance du voyageur:",
            "numero_cni" : "Numéro de la CNI:",
            "numero_passeport" : "Numéro du passeport:",
            "mouvement" : "Description du mouvement:",
            "provenance_destination": "Provenance / Destination:",
            "date_mouvement" : "Date du mouvement:",
            "frontiere" : "Frontière:"
        }

        widgets = {
            "nom" : forms.TextInput(attrs={'placeholder': 'Ex: TOUKO BENEDICTO PACIFICO', 'class': 'form-control form-control-sm'}),
            "date_naissance" : forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'}),
            "numero_cni" : forms.TextInput(attrs={'placeholder': 'Ex: 1234567890', 'class': 'form-control form-control-sm'}),
            "numero_passeport": forms.TextInput(attrs={'placeholder': 'Ex: 1234567890', 'class': 'form-control form-control-sm'}),
            "mouvement": forms.Select(attrs={'class': 'form-control form-control-sm form-select'}),
            "provenance_destination": forms.TextInput(attrs={'placeholder': 'Ex: CANADA', 'class': 'form-control form-control-sm'}),
            "date_mouvement": forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'}),
            "frontiere": forms.Select(attrs={'class': 'form-control form-control-sm form-select'}),
        }


    def clean(self):
        cleaned_data = super(PersonForm, self).clean()
        nom = cleaned_data.get('nom')
        date_naissance = cleaned_data.get('date_naissance')
        date_mouvement = cleaned_data.get('date_mouvement')
        date_sortie = cleaned_data.get('date_sortie')
        numero_cni = cleaned_data.get('numero_cni')
        numero_passeport = cleaned_data.get('numero_passeport')
        provenance_destination = cleaned_data.get('provenance_destination')
        
        if numero_cni == numero_passeport:
            raise forms.ValidationError({"numero_cni": "CNI et passeport doivent avoir des identifiants différents !!!"})

        if not numero_cni.isdigit():
            raise forms.ValidationError({"numero_cni": "Le numéro de la CNI ne doitcontenir que des chiffres !!!"})

        if not numero_passeport.isdigit():
            raise forms.ValidationError({"numero_passeport": "Le numéro du passeport ne doit contenir que des chiffres !!!"})

        # Le nom, la provenance et la destination ne doivent pas contenir des caractères invalides
        invalid_characters = "@_!#$%^&*()<>?/\\|}{~:.,"
        pattern = re.compile(f'[{re.escape(invalid_characters)}]')

        if bool(pattern.search(nom)):
            raise forms.ValidationError({"nom": "Présence des caractères invalides dans le nom !!!"})

        if bool(pattern.search(provenance_destination)):
            raise forms.ValidationError({"provenance_destination": "Présence des caractères invalides !!!"})

        # La date de naissance doit être inférieure aux dates d'entrée et de sortie
        if (date_naissance >= date_mouvement):
            raise forms.ValidationError({"date_naissance": "La date de naissance doit être antérieure à la date d'entrée ou de sortie du territoire"})