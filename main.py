# Devine le chiffre

HARD = 5
EASY = 10

from random import randint
from os import system
def trouvenum():
    print("Je pense à un chiffre de 1 à 100")
    number = randint(1,100)
    return number

def setdiff():
    diff = input("Quel niveau vous voulez jouer (f)acile ou (d)ifficile? ")
    if diff == "f":
        return EASY
    else:
        return HARD


def evalue(joueur, cpu):
    if guess == num:
        print(f"Bravo! Le chiffre était bien {num}")
        return 100
    elif guess > num:
        print("Trop haut!")
        return 1
    else:
        print("Trop bas!")
        return 1

trouve = False
rejoue = True

while rejoue:
    print("Bienvenue dans le jeu : Devine le chiffre!")
    num = trouvenum()
    essaie = setdiff()
    while essaie > 0:
        guess = int(input("Quel chiffre pensez-vous? "))
        essaie -= evalue(guess, num)

    if essaie == 0:
        print(f"Désolé vous avez perdu, le chiffre était {num}")
    elif guess == num:
        print(f"Bravo! C'était bien {num}")

    # On rejoue?
    if input("Voulez-vous rejouer (o/n)? : ") == 'o':
        rejoue = True
        trouve = False
        system('cls')
    else:
        rejoue = False
        print("Au Revoir!")
