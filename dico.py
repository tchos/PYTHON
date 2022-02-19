# Les dictionnaires fonctionnent sur forme de {clef:valeur}

# Les clefs sont immutables tandis que les valeurs sont mutables
# Les clefs ne peuvent pas être en doublon mais on peut avoir une même valeur sur plusieurs clefs

# Les valeurs peuvent être de tout type: int, str, list, tuples, dict, ... 
# Déclarer un dictionnaire vide

scores = {} 
scores = dict()

print(scores)
print(type(scores))

# Affecter une valeur à une clef du dict: scores["clef"] = valeur
scores["Kwette"] = 20
scores["Tchos"] = 18
scores["Lolo"] = 17
scores["Milanais"] = 15

print(scores)

# Accéder à la valeur d'une clef d'1 dict: : scores["clef"]
print("Valeur de la clef - Lolo -: {0}".format(scores["Lolo"]))

# Tester si une clef se trouve dans un dict: "clef" in scores
print("lolo" in scores)

# Boucle for sur les clefs d'un dict:
for element in scores:
    print(element)

for element in scores:
    print(element[0])

for clef, valeur in scores.items():
    print(clef)

# Boucle for sur les valeurs d'un dict:
for element in scores:
    print(element[1])

for clef, valeur in scores.items():
    print(valeur)

# Boucle for sur le couple (clef,valeur):
for element in scores.items():
    print(element)

for clef, valeur in scores.items():
    print(clef,valeur)

# dict avec des valeurs sous forme de liste
matches = {}
matches["Ketty"] = [19, 14, 18]
matches["Nathanael"] = [17, 15, 16]

# Afficher la valeur 17 de la liste de la clef "Nathanael"
print (matches["Nathanael"][0])

# Quelques opérations possibles sur les dict
print(type(matches["Ketty"]))
matches["Ketty"].append(13)

# Boucle for sur les listes imbriquées dans un dict
for noms, scores in matches.items():
    print(noms)
    for score in scores:
        print(" * {0}".format(score))