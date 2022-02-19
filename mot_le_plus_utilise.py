#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 06:54:39 2021

@author: tchos
"""

"""
Ce script permet de parcourir tous les fichiers d'un dossier et de lister les mots les plus
utilisés:
    - Importer pathlib pour pouvoir parcourir un dossier
    - Parcourir un dossier via for pour ouvrir un fichier, le lire, l'assainir, compter
        les mots de chaque fichier et stocker le compteur dans un dico
    - Utiliser une boucle for sur le dico pour déterminer le fichier le plus utilisé
"""
# Importation de la librairie pathlib
from pathlib import Path as p

ponctuation = ("'","-","!","«","»",",",";",".","?","<",">","(",")","[","]","{","}","#",'"')

#Initialisation du compteur de mot
compteur = {}

nbreMax = 0
motLePlusUtilise = None

dossier = "/home/tchos/Documents/projets/python/fichiers"

if(p(dossier).exists()):
    """
        On itère sur tous les fichiers qui sont dans le dossier
        on pouvait aussi faire: p(dossier).iterdir()
    """
    for f in p(dossier).glob("*"):
        texte = open(f).read().lower()
        for signe in ponctuation:
            texte.replace(signe," ")
            
        listeMotsFichier = [mot.strip() for mot in texte.split()]
        
        """
        Si le mot est dejà présent dans le dico on incremente son compteur sinon
        on initialise le compteur du mot
        """
        for mot in listeMotsFichier:
            if(mot in compteur):
                compteur[mot] += 1
            else:
                compteur[mot] = 1
                
    """
    On parcours à nouveau le dico pour voir le mot le plus utilisé
    """
    for mot, compte in compteur.items():
        if(nbreMax < compte):
            motLePlusUtilise = mot
            nbreMax = compte
    
    print("Le mot le plus utilisé est {0} avec {1} occurences".
          format(motLePlusUtilise, compteur[motLePlusUtilise]))
       
else:
    print("Le dossier {0} n'existe pas.", format(dossier))