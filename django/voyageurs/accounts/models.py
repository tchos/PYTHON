from django.utils import timezone
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.signals import post_save
from voyageurs import settings

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, nom, telephone, equipe, password=None):
        if not email:
            raise ValueError("L'email de l'utilisateur est obligatoire")
        if not nom:
            raise ValueError("L'utilisateur doit avoir un nom")
        if not telephone:
            raise ValueError("On doit pouvoir contacter un utilisateur")

        user = self.model(
            email=self.normalize_email(email),
            nom=nom,
            telephone=telephone,
            equipe=equipe,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nom, telephone, password=None):
        if not email:
            raise ValueError("L'email de l'utilisateur est obligatoire")
        if not nom:
            raise ValueError("L'utilisateur doit avoir un nom")
        if not telephone:
            raise ValueError("On doit pouvoir contacter un utilisateur")

        user = self.model(
            email=self.normalize_email(email),
            nom=nom,
            telephone=telephone,
        )

        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Team(models.Model):
    """Model pour les équipes de mission"""
    libelle = models.CharField(max_length=64, blank=False, error_messages="Le nom de l'équipe est obligatoire", unique=True)
    chef = models.CharField(max_length=64, blank=False, error_messages="Une équipe doit toujours avoir un chef d'équipe")

    # Tel que ca va apparaitre dans le panneau d'administration de Django
    class Meta:
        verbose_name = "Equipes de mission"
        ordering = ["libelle"]

    # Dans le panneau d'admin des users, ce sont les nom et les email des users qui seront affichés.
    def __str__(self):
        return f"{self.libelle}"


class CustomUser(AbstractBaseUser):
    """Model pour les utilisateurs du système"""
    email = models.EmailField(unique=True, max_length=255, blank=False)
    nom = models.CharField(max_length=64, blank=False, error_messages="Le nom est obligatoire", verbose_name='Nom complet')
    equipe = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    telephone = models.CharField(max_length=32, blank=False, error_messages="Telephone obligatoire", null=False)
    
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date joined', null=True)
    last_login = models.DateTimeField(auto_now_add=True, verbose_name='last login')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # indique le nom du champ devant être utilisé comme identifiant de connexion.
    USERNAME_FIELD = "email"
    # liste des champs à spécifier obligatoirement lors de l’utilisation de la commande  python manage.py createsuperuser
    REQUIRED_FIELDS = ["nom","telephone"]

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # Tel que ca va apparaitre dans le panneau d'administration de Django
    class Meta:
        verbose_name = "Utilisateurs"
        ordering = ["-date_joined"]

    # Dans le panneau d'admin des users, ce sont les nom et les email des users qui seront affichés.
    def __str__(self):
        return f"{self.nom} - {self.email}"

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)