#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 07:26:07 2021

@author: tchos
"""

# Créer une fonction
def nom_de_la_fonction(parametres):
    """Documentation de la fonction"""
    #instructions
    #return
    
# Exple: la fonction qui calcule la moyenne de 2 entiers
def moyenne (a, b):
    """Calcule la moyenne de 2 entiers naturels"""
    return (a + b) / 2

# Voir l'aide sur une fonction: help(nom_de_la_fonction)
help(moyenne)

# Entrer en mode aide: help()

""" 
    Voir les chemins de dossier à partir desquels python ajoute et importe ses modules 
    et ses fonctions
"""
import sys
sys.path

# Ajouter un autre chemin contenant un module python que nous avons développés
chemin = "~/Documents/projets/python/"
sys.path.append(chemin)

# Vérifier si 'limportation a marché
print(sys.path)
