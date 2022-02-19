#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:59:29 2021

@author: tchos
"""

# Ouvrir le fichier en lecture:
fichier = open('/home/tchos/Documents/projets/python/fichiers/chanson.txt')

from mes_fonctions import mots

listeMots = list(mots('/home/tchos/Documents/projets/python/fichiers/chanson.txt'))

for mot in listeMots:
    print(mot)