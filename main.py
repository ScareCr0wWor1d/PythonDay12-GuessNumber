# Devine le chiffre

from random import randint
from os import system
def trouvenum():
    number = randint(1,100)
    return number


trouve = False
rejoue = True

while rejoue:
    print("Bienvenue dans le jeu : Devine le chiffre!")
    num = trouvenum()
    print("Je pense à un chiffre de 1 à 100")
    diff = input("Quel niveau vous voulez jouer (f)acile ou (d)ifficile? ")
    if diff == "f":
        essaie = 10
    else:
        essaie = 5

    while not trouve and essaie > 0:
        guess = int(input("Quel chiffre pensez-vous? "))
        if guess == num:
            print(f"Bravo! Le chiffre était bien {num}")
            trouve = True
        elif guess > num:
            print("Trop haut!")
            essaie -= 1
        elif guess < num:
            print("Trop bas!")
            essaie -= 1
    if essaie == 0:
        print(f"Désolé vous avez perdu, le chiffre était {num}")
    elif guess == num:
        print(f"Bravo! C'était bien {num}")
    if input("Voulez-vous rejouer (o/n)? : ") == 'o':
        rejoue = True
        trouve = False
        system('cls')
    else:
        rejoue = False
        print("Au Revoir!")
