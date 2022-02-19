#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Les listes sont mutables c'est-� -dire modifiables

# Déclarer une liste vide: fruits = [] ou fruits = list()
fruits = []
fruits = list()

# Déclarer une liste d'objet
legumes = ["Tomate", "Salade", "Carotte", "Poire", "Epinard", "Poireau", "Proivron", "Persil", "Aubergine"]

# Afficher une liste
print(fruits)
print(legumes)
print(fruits, legumes)

# Afficher le type d'une liste
print(type(fruits), type(legumes))

# Ajouter un élément �  une liste
fruits.append("Pomme")
print(fruits)

# Accéder �  un objet de la liste �  partir du début: legumes[n]
legumes[1]

# Accéder �  un objet de la liste �  partir de la fin: legumes[-n]
legumes[-1]

# Supprimer le dernier objet de la liste: legumes.pop()
legumes.pop()

# Supprimer l'objet �  l'indice n de la liste: legumes.pop(n)
legumes.pop(1)

# Insérer un objet dans une liste �  partir de la position n: legumes.insert(n, objet)
legumes.insert(1, "Celeri")
print(legumes)

# Remplacer un objet �  un index donné par un autre objet: legumes[3] = objet
legumes[3] = "Ndolè"

# Taille d'une liste : len(legumes)
print(len(legumes))

# Tester si objet se trouve dans une liste: objet in legumes
if ("Celeri" in legumes):
    print(True)
else:
    print(False)

# Récupérer un sous-ensemble d'une liste avec pour pas 1: legumes[n:m]
print(legumes[1:-3])
# Récupérer un sous-ensemble d'une liste avec pour pas x: legumes[n:m:x]
print(legumes[1:7:2])
# Récupérer un sous-ensemble de la position n �  la fin d'une liste: legumes[n:]
# Récupérer un sous-ensemble de la position n au début d'une liste: legumes[:n]
# Inverser l'ordre d'une liste: legumes[::-1]
print(legumes[::-1])

# Transformer un string en liste: list(string)
print(list("Bonjour"))


