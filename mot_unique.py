#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 06:19:14 2021

@author: tchos
"""

"""
Syntaxe qui permet de trouver tous les mots uniques dans un fichier:
    - Ouvrir le fichier
    - Remplacer toutes les chaines de ponctuation par le vide
    - Enlever les espaces dont on aura pas besoin
    - Récupérer individuellement chaque  mot pour l'ajouter à un set
"""

listeMotsUnique = set()

# Ouvrir le fichier en lecture:
fichier = open('/home/tchos/Documents/projets/python/fichiers/chanson.txt')
texte = fichier.read().lower()

# Remplacer toutes les chaines de ponctuation par le vide
texte = texte.replace("'"," ").replace("-"," ").replace("!"," ").replace('«',' ').replace("»"," ")
texte = texte.replace(',',' ').replace('.',' ').replace(';',' ').replace(':',' ').replace('?',' ')

# On pouvait aussi faire comme ceci:
ponctuation = ("'","-","!","«","»",",",";",".","?")

for signe in ponctuation:
    texte.replace(signe, "")

# Enlever les espaces dont on aura pas besoin
listeDeMots = texte.split()

for mot in listeDeMots:
    listeMotsUnique.add(mot.strip())
    
# On pouvait aussi faire comme ceci: transformer la liste en set
listeMotsUnique = set(texte.split())

# Afficher la liste des mots uniques
for mot in listeMotsUnique:
    print(mot)