from django.contrib import admin
from .models import CustomUser, Team

# Register your models here.
# première facon d'ajouter le modele BlogPost à l'interface d'administration: admin.site.register(CustomUser)

"""
deuxième facon d'ajouter le modele BlogPost à l'interface d'administration,
elle est plus utilisée car elle permet plus de personnalisation sur les champs du modèle à afficher
"""

@admin.register(CustomUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "equipe", "telephone", "date_joined", "last_login")
    empty_value_display = "Inconnu"

    # afficher 25 utilisateurs par page
    list_per_page = 25

    # Liste des champs éditables:
    list_editable = ("email",)

    # Quels champs seront cliquables pour consulter un user:
    list_display_links = ("nom",)

    # ajouter un filtre de recherche
    search_fields = ("nom", )
    list_filter = ("nom", "equipe",)

    # créer un champ autocomplete
    autocomplete_fields = ("equipe",)

@admin.register(Team)
class TeamUserAdmin(admin.ModelAdmin):
    list_display = ("libelle", "chef",)
    empty_value_display = "Inconnu"

    # afficher 10 équipes par page
    list_per_page = 10

    # Liste des champs éditables:
    list_editable = ("chef", )

    # Quels champs seront cliquables pour consulter un user:
    list_display_links = ("libelle",)

    # ajouter un filtre de recherche
    search_fields = ("libelle",)
    list_filter = ("libelle",)
