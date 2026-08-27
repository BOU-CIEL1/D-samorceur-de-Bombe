# Fichier où est mis tout ce qui est lié aux assets graphiques

import pygame # Importer le module Pygame

IMAGES = {} # Dictionnaire contenant tous les assets graphiques

def charger_assets():
  # Charge et redimensionne tous les assets du jeu

  # Image de la bombe
  image_bombe_origin = pygame.image.load("images/bombe.jpg").convert_alpha() # Implémentation d'une image dans l'écran en la convertissant dans le format le plus adapté niveau vitesse

  # Récupérer les dimensions de l'image originale
  rect = image_bombe_origin.get_rect()
  largeur_origin = rect.width
  hauteur_origin = rect.height

  # Redimensionner l'image en divisant ses proportions par 10
  new_largeur = largeur_origin // 10
  new_hauteur = hauteur_origin // 10

  IMAGES["bombe"] = pygame.transform.scale(image_bombe_origin, (new_largeur, new_hauteur)) # Redimensionner l'image avec les proportions calculées
