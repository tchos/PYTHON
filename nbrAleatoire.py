# Ce programme permet de dire si le nombre entré par un user est celui généré aléatoirement par l'ordi.

# Importation de la librairie random
import random

# Nbre généré entre 0 et 100
resultat = random.randint(0, 100)

# Liste qui enregistre l'historique des essais du user
essai = []
chance = 5

while(chance > 0):
    # On récupère le nombre entré par le user
    nbreUser = int(input("Dévinez le nombre entier qui a été généré entre 0 et 100: "))
    essai.append(nbreUser)

    if(nbreUser == resultat):
        print("Historique de vos tentatives: {0}". format(essai))
        print("Bravo !!! Vous avez gagné en {0} essai(s).". format(len(essai)))
        print("Le nombre à déviner était {0} !!!\n". format(resultat))
        break

    else:
        if(nbreUser < resultat):
            print("Le nombre à déviner est plus grand\n")
        else:
            print("Le nombre à déviner est plus petit\n")
        chance -= 1
        if(chance == 1):
            print("C'est votre dernière chance de trouver le nombre.\n")
        else:
            print("Il vous reste {0} chance(s) de trouver le nombre.\n". format(chance))
    
if(nbreUser != resultat):
    print("Historique de vos tentatives: {0}". format(essai))
    print("Vous avez échoué après {0} tentattives !!!\n". format(len(essai)))
    print("Le nombre à déviner était {0} !!!\n". format(resultat))


print("Good !!!\n")


