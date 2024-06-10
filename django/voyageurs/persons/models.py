from django.db import models
from accounts.models import CustomUser
from voyageurs import settings

# Create your models here.
class Person(models.Model):
    """Modele sur les agents voyageurs"""
    FRONTIERES_CHOICES = (
        (1, 'AEROPORT DE NSIMALEN'),
        (2, 'AEROPORT DE DOUALA'),
        (3, 'AEROPORT DE GAROUA ET BANKI'),
        (4, 'FRONTIERE DE ELOK'),
        (5, 'FRONTIERE DE IDENAU'),
        (6, 'FRONTIERE DE ABANG MINKO'),
        (7, 'FRONTIERE DE KYE OSSI'),
        (8, 'DONNEES CNPS'),
    )

    MOUVEMENT_CHOICES = (
        (1, 'ENTREE'),
        (2, 'SORTIE')
    )

    nom = models.CharField(max_length=64, null=False, blank=False)
    date_naissance = models.DateField()
    numero_cni = models.CharField(max_length=32, null=False, blank=False)
    numero_passeport = models.CharField(max_length=32, null=True, blank=True)
    mouvement = models.PositiveSmallIntegerField(choices=MOUVEMENT_CHOICES, null=True, blank=True)
    date_mouvement = models.DateField()
    provenance_destination = models.CharField(max_length=64, null=False, blank=False)
    frontiere = models.PositiveSmallIntegerField(choices=FRONTIERES_CHOICES, null=True, blank=True)
    collector = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    date_saisie = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} NEE LE {self.date_naissance}"
