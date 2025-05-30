# Importation de la bibliothèque pygame
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

# Création des variables pour gérer le temps d’affichage des lumières du Simon
start_time_vert = 0
start_time_rouge = 0
start_time_bleu = 0
start_time_jaune = 0
duration = 500

# Régler la vitesse du jeu
clock = pygame.time.Clock()

# Fermer le jeu au moment voulu + Allumer les lumière et jouer les sondu Simon quand on clique dessus
runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if vert_rect.collidepoint(event.pos):
                start_time_vert = pygame.time.get_ticks()
                vert.set_alpha(255)
                pygame.mixer.music.load("audio/vert.wav")
                pygame.mixer.music.play(1)
            elif rouge_rect.collidepoint(event.pos):
                start_time_rouge = pygame.time.get_ticks()
                rouge.set_alpha(255)
                pygame.mixer.music.load("audio/rouge.wav")
                pygame.mixer.music.play(1)
            elif bleu_rect.collidepoint(event.pos):
                start_time_bleu = pygame.time.get_ticks()
                bleu.set_alpha(255)
                pygame.mixer.music.load("audio/bleu.wav")
                pygame.mixer.music.play(1)
            elif jaune_rect.collidepoint(event.pos):
                start_time_jaune = pygame.time.get_ticks()
                jaune.set_alpha(255)
                pygame.mixer.music.load("audio/jaune.wav")
                pygame.mixer.music.play(1)
    
# Afficher toutes les images au coordonné voulu
    clock.tick(60)
    pygame.display.flip()
    screen.blit(fond, (0,0))
    screen.blit(simon, rect)
    screen.blit(vert, vert_rect)
    screen.blit(rouge, rouge_rect)
    screen.blit(bleu, bleu_rect)
    screen.blit(jaune, jaune_rect)

# Afficher les lumières pendant un temps déterminé
    current_time = pygame.time.get_ticks()
    if current_time - start_time_vert >= duration:
        vert.set_alpha(0)
    
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


