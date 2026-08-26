# Fichier où est mis tout ce qui est en rapport avec la logique de code de base du jeu

# L'ordinateur choisit un nombre aléatoire entre 1 et 3
# Le programme affiche un message "Quel fil couper? (1, 2 ou 3)"
# Saisir le nombre dans la console
# Si nombre égal au nombre secret: afficher "Victoire! La bombe est désamorcée!"
# Sinon: afficher "BOOM! Mauvais fil..."

import random

MINIMUM = 1
FACILE = 3
NORMAL = 4
DIFFICILE = 5
GAME_OVER = 0
DEPART_INFINI = 3

# Création d'un dictionnaire avec les paramètres à manipuler dans le code pour pouvoir les utiliser n'importe où dans le code
parametres = {
  "lives": 2
}

def mode():
  while True:
    try:
      # L'utilisateur doit choisir entre jouer dans le mode de jeu classique et le mode de jeu infini
      print("Choisis ton mode de jeu: \n" \
      f"(1) Mode classique \n" \
      f"(2) Mode infini")
      modeChoisi = int(input())

      # Si l'utilisateur a choisi le mode classique, il devra choisir sa difficulté, s'il choisit le mode infini, la partie se lance directement
      if modeChoisi == 1:
        difficulte()
        break
      elif modeChoisi == 2:
        infini(DEPART_INFINI)
        break
      else:
        print("Erreur! Recommencez!")
    except ValueError:
      print("Erreur! Recommencez!")

def difficulte():
  while True:
    try:
      # L'utilisateur doit choisir son mode de difficulté entre 3 modes
      print("Choisis ton mode de difficulté: \n" \
      f"(1) Facile: {FACILE} fils \n" \
      f"(2) Normal: {NORMAL} fils \n" \
      f"(3) Difficile: {DIFFICILE} fils \n")
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

  while parametres["lives"] > GAME_OVER: # Tant que l'utilisateur a encore des vies

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
      return
    else:
      lives() # Déclenchement de la fontion lives() quand l'utilisateur se trompe

def lives():
  parametres["lives"] -= 1 # L'utilisateur perd une vie s'il se trompe

  if parametres["lives"] > GAME_OVER:
    print(f"Mauvais fil, il ne te reste plus que {parametres["lives"]} vie.") # Message quand on pert une vie
  else:
    print("GAME OVER!") # Défaite si 0 vie

def infini(nbFils):
  parametres["lives"] = 3 # Le mode infini commence avec 3 vies
  niveau = 1 # On commence au niveau 1
  
  print("Bienvenue dans le mode infini! Les règles sont simples: \n" \
  "Vous commencez avec 3 vies. Si vous couper le mauvais fil vous perdez une vie. Tous les 5 niveaux, le jeu vous rend une vie mais en contre-partie, une bombe est rajoutée. \n" \
  "Le but est de rester en vie le plus de niveaux possible. Bonne chance!")

  input("Appuis sur ENTREE pour démarrer!") # Le mode se lance quand l'utilisateur appuie sur ENTREE

  while parametres["lives"] > GAME_OVER: # Tant que l'utilisateur a encore des vies

    if niveau > 1 and (niveau - 1) % 5 == 0: # Augmente le nombre de fil et le nombre de vies de 1 tous les 5 niveaux
      parametres["lives"] += 1
      print("Palier de 5 niveaux atteint! Vous gagnez une vie!")

    print(f"\n--- NIVEAU {niveau} (Vies restantes: {parametres['lives']}) ---") # Message qui affiche le niveau actuel et le nombre de vies actuel


    nbFils = DEPART_INFINI + (niveau - 1) // 5 # Comment le programme calcule le nombre de fils par niveau. Il commence à 3 et augmente de 1 tous les 5 niveaux
    nombreSecret = random.randint(MINIMUM, nbFils) # Génération d'un nombre aléatoire
    bombeValide = False # Cette variable permet de détecter si la bombe a bien été désamorcée (si le niveau a été réussi)

    # Le niveau se lance tant que l'utilisateur a encore des vies et que la bombe n'a pas été désamorcée (niveau pas encore réussi)
    while parametres["lives"] > GAME_OVER and not bombeValide:

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
        print("Bravo! Passons au niveau suivant!") # Résultat en cas de victoire
        bombeValide = True # La bombe a été désamorcée donc la variable devient True, le niveau est réussi
      else:
        lives() # Déclenchement de la fontion lives() quand l'utilisateur se trompe

    if parametres["lives"] == GAME_OVER: # Affiche un message de défaite quand l'utilisateur n'a plus de vie
      print(f"Vous avez succombé au niveau {niveau}.")

    if bombeValide: # Le niveau du jeu augmente de 1 quand il a été réussi
      niveau += 1

mode()