#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sat May  8 07:55:40 2021

    @author: tchos

    Contient les fonction dévéloppées par Tchos Lolo le Milanais

"""

# fonction moyenne
def moyenne (a, b):
    """Calcule la moyenne de 2 entiers naturels"""
    return (a + b) / 2

# fonction listing
def listing (liste, bullet="-"):
    """Itère les éléments d'une liste"""
    b = [ print(f"{bullet} {x}") for x in liste ]
    
    # on peut aussi faire: b = [ print("%bullet %x" % (bullet, x)) for x in liste ]
    return b

#print(listing("abcde"))

# fonction qui permet de remplacer les mots d'un fichier par les mots que nous voulons
def censure(fichier1, fichier2, **mots):
    """Cette fonction ouvre un fichier et remplace certains mots par des mots spécifiés"""
    #dossier = "/home/tchos/Documents/projets/python/fichiers/"
    try:
        with open(fichier1) as fichier1:
            with open(fichier2, 'w') as fichier2:
                texte = fichier1.read()
                for mot, remplacer in mots.items():
                    texte = texte.replace(mot, remplacer)
                # On écrit le nouveau texte dans le fichier de destination
                fichier2.write(texte)
    except EnvironmentError:
        print ("Impossibles d'ouvrir le fichier :", fichier1)
    return None

# fonction qui permet de la liste des mots contenus dans un fichier
def mots(*fichiers):
    """Cette fonction génère la liste des mots contenus dans un ou plusieurs fichiers"""
    for fichier in fichiers:
        try:
            with open(fichier) as fichier:
                texte = fichier.read().lower()
    
                # Remplacer toutes les chaines de ponctuation par le vide
                ponctuation = ("'","-","!","«","»",",",";",".","?","<",">","(",")","[","]","{","}","#",'"')
                
                for signe in ponctuation:
                    texte = texte.replace(signe, "")
                
                for x in texte.split():
                    yield x
                
        except EnvironmentError:
            print("Impossible d'ouvrir le fichier {0}", format(fichier))
        
    return None


