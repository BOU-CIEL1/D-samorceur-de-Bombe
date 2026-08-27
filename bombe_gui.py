# Fichier où est mis en place tout ce qui est en rapport avec l'interface graphique et Pygame

import pygame # Importer le module Pygame
from assets import IMAGES, charger_assets # Importer le fichier des assets et le dictionnaire les contenant

pygame.init() # Initialiser tous les modules présent dans Pygame pour gagner en vitesse

screen = pygame.display.set_mode((1000, 1000)) # Création d'une fenêtre

running = True # Création d'un booléen pour vérifier si la fenêtre de jeu est ouverte ou fermée
charger_assets()

x = 0
y = 0

clock = pygame.time.Clock()


while running:
  for event in pygame.event.get(): # Vérifie si un événement a été lancé
    if event.type == pygame.QUIT: # Met la variable running à False si l'événement de quitter la fenêtre est lancé
      running = False

  pressed = pygame.key.get_pressed() # Import du dictionnaire get_pressed()
  if pressed[pygame.K_LEFT]: # Si la flèche de gauche est enfoncée
    x -= 1
  if pressed[pygame.K_RIGHT]: # Si la flèche de droite est enfoncée
    x += 1
  if pressed[pygame.K_UP]: # Si la flèche de haut est enfoncée
    y -= 1
  if pressed[pygame.K_DOWN]: # Si la flèche de bas est enfoncée
    y += 1

  screen.fill((0, 0, 0)) # Remplir l'écran en noir
  screen.blit(IMAGES["bombe"], (x, y)) # Afficher l'image aux coordonnées données
  pygame.display.flip() # Mettre à jour l'écran
  clock.tick(60) # Faire tourner la boucle de jeu à 60 FPS

pygame.quit() # Quitter la fenêtre