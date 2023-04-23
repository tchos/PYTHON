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

# Installer un nouveau package
pip install package
conda install -c conda-forge package

"""
7 étapes pour installer un package Python dans Anaconda Navigator:
	1. Avec le démarrage de l'Anaconda Navigator, appuyez sur «Environnement».
	2. Sélectionnez votre environnement, créez-en un nouveau ou laissez-le tel quel (environnement de base)
	3. Cliquez sur le menu déroulant
	4. Cliquez sur "Non installé"
	5. Recherchez Pandas et appuyez sur Entrée
	6. Cliquez sur l'icône de vérification, lorsque Pandasis a trouvé
	7. Cliquez sur «Appliquer» dans le coin inférieur droit
"""

# Mise à jour all Python Packages using conda
conda update --all

# Lister tous les packages installés avec pip
pip list

