# Cacher le message d'initialisation de pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Importation des bibliothèque
from random import randint
import pygame

# Initialisation des sons
pygame.mixer.init()

# Initialisation de pygame + création de la fenêtre
pygame.init()
screen = pygame.display.set_mode((800,800))

# Nom + Icone de la fenêtre
pygame.display.set_caption("Simon")
icon = pygame.image.load("img/SimonNormal.png").convert_alpha()
pygame.display.set_icon(icon)

# Afficher le fond
fond = pygame.image.load("img/fond.png").convert_alpha()
fond = pygame.transform.scale(fond, (800,800))

# Afficher le Simon
simon = pygame.image.load("img/SimonNormal.png").convert_alpha()
simon = pygame.transform.scale(simon, (600,600))
rect = simon.get_rect()
rect.center = (400,400)

# Afficher la lumière verte
vert = pygame.image.load("img/GreenSimon.png").convert_alpha()
vert = pygame.transform.scale(vert, (285,285))
vert.set_alpha(0)
vert_rect = vert.get_rect()
vert_rect.center = (243.75,245)

# Afficher la lumière rouge
rouge = pygame.image.load("img/RedSimon.png").convert_alpha()
rouge = pygame.transform.scale(rouge, (285,285))
rouge.set_alpha(0)
rouge_rect = rouge.get_rect()
rouge_rect.center = (553.25,250)

# Afficher la lumière bleu
bleu = pygame.image.load("img/BlueSimon.png").convert_alpha()
bleu = pygame.transform.scale(bleu, (285,285))
bleu.set_alpha(0)
bleu_rect = bleu.get_rect()
bleu_rect.center = (553.25,555.25)

# Afficher la lumière jaune
jaune = pygame.image.load("img/YellowSimon.png").convert_alpha()
jaune = pygame.transform.scale(jaune, (285,285))
jaune.set_alpha(0)
jaune_rect = jaune.get_rect()
jaune_rect.center = (243.75,555.25)

# Création des variables pour gérer le temps d'affichage des lumières du Simon
start_time_vert = 0
start_time_rouge = 0
start_time_bleu = 0
start_time_jaune = 0
start_time = 0
duration = 500
delai_entre_couleur = 800  # Délai entre chaque couleur en millisecondes

# Initialisation des variables selon l'algorigramme
sequence = []  
nb_essais = 0
perdu = False
afficher_sequence = False
position_sequence = 0
past_time = 0

# Afficher le score
font_path = "joystix monospace.otf"
font = pygame.font.Font(font_path, 24)
text_color = (255, 255, 255)
best_score = 0

# Régler la vitesse du jeu
clock = pygame.time.Clock()

# Boucle principale
runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
        
        if perdu:
            sequence = []
            nb_essais = 0
            perdu = False
            afficher_sequence = False
            
        # Si on ne montre pas la séquence
        else:
            # Vérifier si le joueur a complété la séquence actuelle
            if nb_essais == len(sequence):
                sequence.append(randint(1,4))  # Ajouter une couleur à la séquence
                afficher_sequence = True  # Afficher la séquence
                position_sequence = 0
                past_time = pygame.time.get_ticks()
                nb_essais = 0  # Réinitialiser le nombre d'essais
            
            # Gestion des clics du joueur
            elif event.type == pygame.MOUSEBUTTONDOWN:
                saisis_joueur = 0
                if vert_rect.collidepoint(event.pos):
                    saisis_joueur = 2
                    start_time_vert = pygame.time.get_ticks()
                    vert.set_alpha(255)
                    pygame.mixer.music.load("audio/vert.wav")
                    pygame.mixer.music.play(1)
                elif rouge_rect.collidepoint(event.pos):
                    saisis_joueur = 1
                    start_time_rouge = pygame.time.get_ticks()
                    rouge.set_alpha(255)
                    pygame.mixer.music.load("audio/rouge.wav")
                    pygame.mixer.music.play(1)
                elif bleu_rect.collidepoint(event.pos):
                    saisis_joueur = 3
                    start_time_bleu = pygame.time.get_ticks()
                    bleu.set_alpha(255)
                    pygame.mixer.music.load("audio/bleu.wav")
                    pygame.mixer.music.play(1)
                elif jaune_rect.collidepoint(event.pos):
                    saisis_joueur = 4
                    start_time_jaune = pygame.time.get_ticks()
                    jaune.set_alpha(255)
                    pygame.mixer.music.load("audio/jaune.wav")
                    pygame.mixer.music.play(1)
                
                # Vérification de la saisie du joueur
                if saisis_joueur != 0:
                    if saisis_joueur == sequence[nb_essais]:
                        nb_essais += 1 
                    else:
                        perdu = True
                        if len(sequence) - 1 > best_score:
                            best_score = len(sequence) - 1

    # Gestion de l'affichage de la séquence
    if afficher_sequence:
        current_time = pygame.time.get_ticks()
        if current_time - past_time >= delai_entre_couleur:
            if position_sequence < len(sequence):
                # Affichage de chaque couleur de la séquence
                if sequence[position_sequence] == 1:
                    start_time_rouge = current_time
                    rouge.set_alpha(255)
                    pygame.mixer.music.load("audio/rouge.wav")
                    pygame.mixer.music.play(1)
                elif sequence[position_sequence] == 2:
                    start_time_vert = current_time
                    vert.set_alpha(255)
                    pygame.mixer.music.load("audio/vert.wav")
                    pygame.mixer.music.play(1)
                elif sequence[position_sequence] == 3:
                    start_time_bleu = current_time
                    bleu.set_alpha(255)
                    pygame.mixer.music.load("audio/bleu.wav")
                    pygame.mixer.music.play(1)
                elif sequence[position_sequence] == 4:
                    start_time_jaune = current_time
                    jaune.set_alpha(255)
                    pygame.mixer.music.load("audio/jaune.wav")
                    pygame.mixer.music.play(1)
                position_sequence += 1
                past_time = current_time
            else:
                afficher_sequence = False

    # Mettre à jour le texte du score
    text = f"Score : {len(sequence) - 1}"
    text_surface = font.render(text, True, text_color)
    text_surface.set_alpha(200)
    text_rect = text_surface.get_rect(center=(100, 20))

    # Mettre à jour le texte du meilleur score
    best_score_text = f"Meilleur score : {best_score}"
    best_score_surface = font.render(best_score_text, True, text_color)
    best_score_surface.set_alpha(200)
    best_score_rect = best_score_surface.get_rect(center=(580, 770))
    
    # Afficher toutes les images aux coordonnées voulues
    clock.tick(60)
    pygame.display.flip()
    screen.blit(fond, (0,0))
    screen.blit(simon, rect)
    screen.blit(vert, vert_rect)
    screen.blit(rouge, rouge_rect)
    screen.blit(bleu, bleu_rect)
    screen.blit(jaune, jaune_rect)
    screen.blit(text_surface, text_rect)
    screen.blit(best_score_surface, best_score_rect)
    
    # Afficher les lumières pendant un temps déterminé
    current_time = pygame.time.get_ticks() # prend le temps
    if current_time - start_time_vert >= duration: # vérifie si la durée voulue est dépassée 
        vert.set_alpha(0) # fait disparaitre l'image 
    
    current_time = pygame.time.get_ticks()
    if current_time - start_time_rouge >= duration:
        rouge.set_alpha(0)
    
    current_time = pygame.time.get_ticks()
    if current_time - start_time_bleu >= duration:
        bleu.set_alpha(0)
        
    current_time = pygame.time.get_ticks()
    if current_time - start_time_jaune >= duration:
        jaune.set_alpha(0)

# Arrêter pygame
pygame.quit()