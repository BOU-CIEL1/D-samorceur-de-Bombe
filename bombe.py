# L'ordinateur choisit un nombre aléatoire entre 1 et 3
# Le programme affiche un message "Quel fil couper? (1, 2 ou 3)"
# Saisir le nombre dans la console
# Si nombre égal au nombre secret: afficher "Victoire! La bombe est désamorcée!"
# Sinon: afficher "BOOM! Mauvais fil..."

import random
MINIMUM = 1
FACILE = 2
NORMAL = 3
DIFFICILE = 5

def difficulte():
  while True:
    try:
      # L'utilisateur doit choisir son mode de difficulté entre 3 modes
      print("Choisis ton mode de difficulté: \n" \
      "(1) Facile: 2 fils \n" \
      "(2) Normal: 3 fils \n" \
      "(3) Difficile: 5 fils \n")
      difficulteChoisie = int(input())

      # La difficulté est choisie en fonction de ce que rentre l'utilisateur et démarre le jeu
      if difficulteChoisie == 1:
        bombe(FACILE) # Déclenche le mode facile
        break
      elif difficulteChoisie == 2:
        bombe(NORMAL) # Déclenche le mode normal
        break
      elif difficulteChoisie == 3:
        bombe(DIFFICILE) # Déclenche le mode difficile
        break
      else:
        print("Erreur! Recommencez!") # Couvre les erreurs d'intervalle
    except ValueError:
      print("Erreur! Recommencez!") # Couvre les erreurs de types de valeur

def bombe(nbFils):

  # Création d'un nombre aléatoire dans un intervalle prévu à l'avance
  nombreSecret = random.randint(MINIMUM, nbFils)

  # Boucler tant que l'utilisateur n'a rien écrit
  while True:
    try:
      print(f"Quel fil couper? ({MINIMUM} à {nbFils})")
      nombreChoisi = int(input())

      # Couvre les erreurs d'intervalles de nombre (si l'utilisateur n'a pas écris un nombre entre les valeurs demandées)
      if MINIMUM <= nombreChoisi <= nbFils:
        break # Saisie correcte donc on sort de la boucle while
      else:
        print("Erreur! Recommencez!") # Saisie incorrecte, l'utilisateur doit recommencer

    # Couvre les erreurs de types de valeur (si l'utlisateur écrit une chaine de caractères par exemple au lieu d'un entier)
    except ValueError:
      print("Erreur! Recommencez!")

  if nombreChoisi == nombreSecret:
    print("Victoire! La bombe est désamorcée!") # Résultat en cas de victoire
  else:
    print("BOOM! Mauvais fil...") # Résultat en cas de défaite

difficulte()