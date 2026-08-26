# Fichier où est mis en place tout ce qui est en rapport avec l'interface graphique et Pygame

import pygame # Importer le module Pygame

pygame.init() # Initialiser tous les modules présent dans Pygame pour gagner en vitesse

pygame.display.set_mode((400, 400)) # Création d'une fenêtre

running = True # Création d'un booléen pour vérifier si la fenêtre de jeu est ouverte ou fermée

while running:
  for event in pygame.event.get(): # Vérifie si un événement a été lancé
    if event.type == pygame.QUIT: # Met la variable running à False si l'événement de quitter la fenêtre est lancé
      running = False

pygame.quit() # Quitter la fenêtre