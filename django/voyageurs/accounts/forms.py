from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from .models import CustomUser, Team

class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'minfi'}))
    class Meta:
        model = CustomUser
        fields = ['nom', 'email', 'telephone', 'equipe', 'password', 'confirm_password']

        # Personnalisation des champs du formulaire
        labels = {
            'nom': "Nom complet de l'utilisateur :",
            'email': "Adresse email :",
            'equipe':'Equipe de mission :',
            'telephone':'Telephone :',
            'password': 'Mot de passe :',
            'confirm_password': 'Confirmer le mot de passe :'
        }

        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Ex: ELOHIM MELCHISEDEK'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ex: kwenol@minfi.cm'}),
            'telephone': forms.TextInput(attrs={'placeholder': 'Ex: 620202020'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'minfi'}),
        }

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        email = cleaned_data.get('email')

        if password != confirm_password:
            raise forms.ValidationError({"password":"Erreur: Les mots de passes sont différents !!!"})

        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError({"email":"Erreur: Cet email existe déjà. Veuillez utiliser une autre adresse email !!!"})


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
        # Personnalisation des champs du formulaire
        labels = {
            'libelle': "Libellé de l'équipe :",
            'chef': "Nom du chef d'équipe :"
        }

        widgets = {
            'libelle': forms.TextInput(attrs={'placeholder': 'Ex: FRONTIERE DE KYE-OSSI'}),
            'chef': forms.TextInput(attrs={'placeholder': 'Ex: ELOHIM MELCHISEDEK'})
        }

class LoginForm(AuthenticationForm):
    #username = UsernameField(label='Nom utilisateur', widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    username = UsernameField(widget=forms.EmailInput(attrs={
        'placeholder': 'EX: votrenom@minfi.cm',
        'class': 'form-control form-control-sm'
    }), label='Login de connexion')

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ex: minfi',
        'class': 'form-control form-control-sm'
    }), label='Mot de passe')
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(_("Votre compte est inactif"), code='inactive')