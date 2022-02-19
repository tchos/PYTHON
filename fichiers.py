#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 05:28:41 2021

@author: tchos
"""

# Ouvrir un fichier en lecture:
fichier = open('/home/tchos/Documents/projets/python/fichiers/chanson.txt')

# lire un fichier:
fichier.read()

# lire les 100 1er caractères du fichier
texte = fichier.read(100)

"""
Si on fait encore texte = fichier.read(100), ca chargera les 100 caractères suivants
jusqu'à la fin du fichier
"""

# Reprendre la lecture d'un fichier à partir du début
fichier.seek(0)

# Une fois qu'on a fait fichier.seek(0), on peut reprendre la lecture
texte = fichier.read(100)

# Parcourir un fichier ligne après ligne avec une boucle for:
fichier.seek(0)

for ligne in fichier:
    print(ligne, end="\n") # end="" spécifie le séparateur des lignes

# Avant d'ouvrir le fichier dans un autre mode, il faut d'abord le fermer:
fichier.close()

# Ouvrir un fichier en écriture avec suppression du contenu si l'on écrit:
fichier = open('/home/tchos/Documents/projets/python/fichiers/chanson.txt', 'w')

# Ecrire dans un fichier
fichier.write("Bonjour Tchos")

fichier.close()
fichier = open('/home/tchos/Documents/projets/python/fichiers/chanson.txt')
for ligne in fichier:
    print(ligne, end="\n")


fichier.close()

# Ouvrir un fichier en écriture en permettant d'ajouter du contenu si l'on écrit:
fichier = open('/home/tchos/Documents/projets/python/fichiers/chanson.txt', 'a')

# Ecrire dans un fichier
fichier.write("Bonjour Abigaël")

fichier.close()
fichier = open('/home/tchos/Documents/projets/python/fichiers/chanson.txt')
for ligne in fichier:
    print(ligne, end="\n")
    
''''
 Récupérer tous les mots d'un fichier: texte.split ("separateur")
 Le séparateur par défaut étant l'espace on peut faire : texte.split()
 split renvoi tous les mots d'un fichier sous de liste
'''
fichier = open('/home/tchos/Documents/projets/python/fichiers/chanson.txt', 'a')
fichier.split()

#Remplacer un caractère par un autre caractère: 
fichier.replace('a','b').replace('c','d')

# Ouvrir un fichier en capturant l'exception
try:
    with open('/home/tchos/Documents/projets/python/fichiers/chanson.txt') as fichier:
        print(fichier.read())
except EnvironmentError as e:
    print('Impossibel d\'ouvrir le fichier :', e)


