import random
import pygame
import time


class Enemies:

    # ceci est appelé lors de la création de la vague d'ennemis ! C'est ici que tout est initialisé
    def __init__(self):
        self.enemies = []
        self.nb_moves = 100
        self.curr_move = 0
        self.curr_dir = 1
        self.shot_clock = []
        self.shot_times = []
        self.shot_speed = 5
        self.bullets = []
        self.meteor = pygame.image.load("assets/meteorite.png")
        self.meteor = pygame.transform.scale(self.meteor, (50, 70))
        self.star = pygame.image.load("assets/etoile.png")
        self.star = pygame.transform.scale(self.star, (30, 30))
        self.meteor_probability = 10 / 8

    # crée les images des ennemis
    def select_image(self, x, y):
        # utilise les 4 images correspondantes aux 4 éléments
        image_id = [
            "assets/feu.png",
            "assets/vent.png",
            "assets/terre.png",
            "assets/eau.png"
        ]
        # choisi aléatoirement l'une des 4 images, la première étant à l'index '0'
        return [img, x, y]

    # associe un comportement aux ennemis
    def create_enemies(self):
        for line in range(3):  # numéro de la ligne
            for column in range(10):  # numéro de la colonne
                self.enemies.append(self.select_image(100 * column + 100, 100 * line))  # ajoute un ennemi
                """
                self.shot_times.append(random.randint(1000, 5000))  # permet à l'ennemi d'attaquer à partir d'un certain temps
                self.shot_clock.append(time.time() * 1000)  # permet de donner une cadence de tir à l'ennemi
                """

    # fait tirer les ennemis
    def shot(self):
        """
        for index, enemy in enumerate(self.enemies):  # parcours le "tableau" d'ennemis
            time_now = time.time() * 1000
            if time_now - self.shot_clock[index] > self.shot_times[index]:  # quand le chrono est atteint
                self.shot_clock[index] = time_now
                self.shot_times[index] = random.randint(1000, 5000)  # attend aléatoirement entre 1 à 5 secondes avant de tirer
                if random.randint(0, 100) < 30:  # donne 30% de chances de tirer
                    if random.randint(0, 100) < self.meteor_probability:  # vérifie si le pourcentage de chance de tirer un météore est atteint
                        self.bullets.append([self.meteor, enemy[1], enemy[2], "meteor"])
                    else:  # lance un étoile le cas échéant
                        self.bullets.append([self.star, enemy[1], enemy[2], "star"])
        """
    # même système que pour les projectiles du joueur, c'est ici que sont supprimés les projectiles
    def update_shot(self):
        saved_bullets = []
        for i in range(len(self.bullets)):
            if self.bullets[i][2] < 900:
                self.bullets[i][2] += self.shot_speed
                saved_bullets.append(self.bullets[i])
        self.bullets = saved_bullets

    # permet de faire bouger la vague d'ennemis
    def update(self):
        """
        self.curr_move += "remplace-moi par une valeur !"
        if "remplace-moi par une condition !":
            self.curr_move = "remplace-moi par une valeur !"
            if self.curr_dir == "remplace-moi par une valeur !"
                self.curr_dir = -"remplace-moi par une valeur !"
            else:
                self.curr_dir = "remplace-moi par une valeur !"
            for i in range(len(self.enemies)): # pour la position 'y' de tous les ennemis
                self.enemies[i][2] += "remplace-moi par une valeur !"

        for i in range(len(self.enemies)):  # pour la position 'x' de tous les ennemis
            self.enemies[i][1] += "remplace-moi par une variable contenu dans __init__ !"
        """
        # utilise les 2 fonctions précédentes pour gérer les tirs
        #self.shot()
        #self.update_shot()

    # affiche les ennemis et leurs projectiles
    def display(self, screen):
        for bullet in self.bullets:
            screen.blit(bullet[0], (bullet[1], bullet[2]))
        for enemy in self.enemies:
            screen.blit(enemy[0], (enemy[1], enemy[2]))

    # vérifie si un ennemi est touché par le joueur
    def bullet_collide(self, x, y):
        for index, enemy in enumerate(self.enemies):
            # détruit ce qui est relié à un ennemi, donc lui-même et les chronos associés
            if enemy[1] <= x + "valeur" <= enemy[1] + "valeur" and enemy[2] <= y + "valeur" <= enemy[2] + "valeur":
                del self.enemies[index]
                #del self.shot_clock[index]
                #del self.shot_times[index]
                return True
        return False

    # vérifie si un projectile a touché le joueur
    def player_collision(self, x, y):
        # si le joueur entre en collision avec un ennemi
        for i, e in enumerate(self.enemies):
            if e[1] <= x + "valeur" <= e[1] + "valeur" and e[2] <= y + "valeur" <= e[2] + "valeur":
                del self.enemies[i]
                return -1
        # si le joueur entre en collision avec un projectile
        for i, b in enumerate(self.bullets):
            # météore
            if b[3] == "meteor":
                if b[1] <= x + "valeur" <= b[1] + "valeur" and b[2] <= y + "valeur" <= b[2] + "valeur":
                    del self.bullets[i]
                    return 3
            # étoile
            else:
                if b[1] <= x + "valeur" <= b[1] + "valeur" and b[2] <= y + "valeur" <= b[2] + "valeur":
                    del self.bullets[i]
                    return 1
        return 0
