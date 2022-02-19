#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 04:47:15 2021

@author: tchos
"""

"""
Particularité d'un set:
    - il ne peut pas avoir de doublon dans un set
    - le set ne peut prendre que des objets non mutables (string, tuples, mais pas les listes)
    - les sets sont mutables mais ne sont pas indexables, ni sliceable, mais itérables
"""

# Déclarer un set
ensemble = set()

# voir type d'un set: type(ensemble)
type(ensemble)

# Ajouter un objet dans un set: ensemble.add(objet)
ensemble.add(1)
ensemble.add(1)
ensemble.add(2)
ensemble.add(2)
ensemble.add(4)

# Afficher le contenu d'un set:
print(ensemble)

# Savoir si un objet se trouve dans un set: objet in set
3 in ensemble

# On peut combiner les sets et effectuer des opérations simultanément sur plusieurs sets
a = set([1,2,3,4])
b = set([3,6,4,8])

# Intersection entre l'ensemble a et l'ensemble b: a & b
print("Intersection de a et de b:",a & b)

# Les objets présents dans a, présents dans b mais pas à la fois dans a et b: a ^ b
print("présents dans a, présents dans b mais pas à la fois dans a et b:", a ^ b)

# Union de deux ensembles: a | b
print("Union de a et de b:", a | b)