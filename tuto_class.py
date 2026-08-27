import pygame
from tuto_player import Player

class Game:
  def __init__(self, screen): # Fonction d'initialisation du jeu
    self.screen = screen
    self.running = True
    self.clock = pygame.time.Clock()
    self.player = Player(0, 0)
    self.area = pygame.Rect(300, 150, 300, 300)
    self.area_color = "red"

  def handling_events(self): # Fonction qui gère les événements du jeu
    for event in pygame.event.get(): # Vérifie si un événement a été lancé
      if event.type == pygame.QUIT: # Met la variable running à False si l'événement de quitter la fenêtre est lancé
        self.running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.player.velocity[0] = -1
    elif keys[pygame.K_RIGHT]:
      self.player.velocity[0] = 1
    else:
      self.player.velocity[0] = 0

    if keys[pygame.K_UP]:
      self.player.velocity[1] = -1
    elif keys[pygame.K_DOWN]:
      self.player.velocity[1] = 1
    else:
      self.player.velocity[1] = 0


  def update(self): # Fonction qui gère la logique du jeu
    self.player.move()
    if self.area.colliderect(self.player.rect):
      self.area_color = "blue"
    else:
      self.area_color = "red"

  def display(self): # Fonction qui gère l'affichage du jeu
    self.screen.fill("white")
    pygame.draw.rect(self.screen, self.area_color, self.area)
    self.player.draw(self.screen)
    pygame.display.flip()
        
  def run(self): # Fonction qui gère le jeu en général
    while self.running:
      self.handling_events()
      self.update()
      self.display()
      self.clock.tick(60)

pygame.init()
screen = pygame.display.set_mode((1080, 720)) # Création d'une fenêtre
game = Game(screen)
game.run()

pygame.quit()