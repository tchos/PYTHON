#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 08:34:59 2021

@author: tchos
"""

# l'unpacking: tester les codes ci-dessus pour comprendre commment fonctionne l'unpacking
a, b, c = "123"

a, b, *c = range(1, 100, 10)

a, *b, c = range(1, 100, 5)

*a, b, c = range(1, 100)

a = b = c = 5

# On peut aussi faire l'unpacking sur les paramètres d'une fonction
def ajouter (a = 0, b = 0):
    """Faire l'addition de 2 nombres entiers naturels"""
    return (a + b)

valeurs = (2, 3)
print(ajouter(valeurs[0], valeurs[1]))

# Avec l'unpacking sur le tuple valeur on aura les mêmes résultats
print(ajouter(*valeurs))

# Avec l'unpacking sur le dico valeur on aura les mêmes résultats
valeurs = {"a": 2, "b": 3}
print(ajouter(**valeurs))
