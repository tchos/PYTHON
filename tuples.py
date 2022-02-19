# Les tuples fonctionnent comme les listes mais ils sont immutables c'est-à-dire qu'on ne peut modifier leur contenu

# Déclarer un tuple vide: couleurs = () ou couleurs = tuple()
couleurs = ()
couleurs = tuple()

# Déclarer un tuple d'objet
couleurs = ("Bleu","Vert","Rouge","Jaune","Blanc","Noir","Rose","Violet","Maron")

# On peut convertir une liste en tuple et inversement
couleurs = list(couleurs)
couleurs = tuple(couleurs)

# Afficher le contenu d'un tuple:
print(couleurs)

# Itérer un tuple
for couleur in couleurs:
    print(couleur)
    
# Ordre inverse du tuple
for couleur in couleurs[::-1]:
    print(couleur)