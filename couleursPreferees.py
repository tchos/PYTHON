#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 06:43:54 2021

@author: tchos
"""

# Création du dict couleur
couleurs = {}
compteur = 0
reponse = None

while reponse != "":
    reponse = input("Quelle est votre couleur préférée ?\n")
    
    # on s'assure que la reponse n'est pas vide car la reponse vide renvoie false
    if reponse:
        if reponse in couleurs:
            couleurs[reponse] = couleurs[reponse] + 1
        else:
            couleurs[reponse] = 1



# On affiche les résultats des couleurs préférées
print("Couleurs préférées:")
for couleur, compteur in couleurs.items():
    print(" * {0} : {1}".format(couleur,compteur))
    