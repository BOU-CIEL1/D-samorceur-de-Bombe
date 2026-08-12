# L'ordinateur choisir un nombre aléatoire entre 1 et 3
# Le programme affiche un message "Quel fil couper? (1, 2 ou 3)"
# Saisir le nombre dans la console
# Si nombre égal au nombre secret: afficher "Victoire! La bombe est désamorcée!"
# Sinon: afficher "BOOM! Mauvais fil..."

import random

def bombe():
  nombreSecret = random.randint(1, 3)
  print("Quel fil couper? (1, 2 ou 3)")
  nombreChoisi = int(input())

  if nombreChoisi == nombreSecret:
    print("Victoire! La bombe est désamorcée!")
  else:
    print("BOOM! Mauvais fil...")

bombe()