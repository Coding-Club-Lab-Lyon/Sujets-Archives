import pygame
from pygame.locals import *
import time
import sys

#### Pour les participants, tout est vide sauf l'init !

class Player:
    # ceci est appelé lors de la création du joueur ! C'est ici que tout est initialisé
    def __init__(self):
        self.img = pygame.image.load("assets/serpentaire.png")
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.x = 0
        self.y = 800
        self.player_speed = 5
        self.bullet_speed = 10
        self.bullets = []
        self.bullet = pygame.image.load("assets/caducee.png")
        self.bullet = pygame.transform.scale(self.bullet, (50, 50))
        self.clock = time.time() * 1000  # millisecondes
        self.shooting_speed = 1  # secondes
        self.hp = 3
        self.font = pygame.font.SysFont(None, 64)
        self.hp_text = "HP : " + str(self.hp)

    # affiche les éléments relatifs au joueur
    def display(self, screen):
        screen.blit(self.img, (self.x, self.y))

    # met à jour les informations relatives au joueur
    def update(self, enemies):
        """
        # vérifie la collision d'un projectile avec le joueur, puis lui retire des points de vie
        damage = enemies.player_collision(self.x, self.y)
        # permet de ne pas avoir de points de vie en négatifs
        if damage == -1:
            self.hp = 0
        else:
            self.hp -= damage
        """
        return # retire-moi quand tu feras des changements ici