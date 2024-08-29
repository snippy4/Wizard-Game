import pygame, Utils, sys
from Animation import Animation

def play_game():
    '''
    LOAD ROOMS
    '''
    room_bg = Utils.load_image("assets/backgrounds/room.png")
    running = True
    while running:
        '''
        DRAW
        '''
        display.blit(room_bg, (0,0))
        screen.blit(pygame.transform.scale(display, screen.get_size()), (0,0))
        pygame.display.flip()


        '''
        ACTIONS
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()          
        if keys[pygame.K_ESCAPE]:
            running = False






pygame.init()
'''
GAME WIDE DEFINITIONS
'''
clock = pygame.time.Clock()
display = pygame.Surface((320, 240))
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #assumes 4:3 aspect ratio may adjust in future
w_ratio = screen.get_width() / display.get_width()
h_ratio = screen.get_height() / display.get_height()
font = pygame.font.Font("assets/fonts/kongtext.ttf", 24)

'''
MENU SCREEN
'''
bg = Utils.load_image("assets/backgrounds/menu bg.png")
cloud_img = Utils.load_image("assets/sprites/cloud 1.png")
clouds = [(60, 40),(80, 194),(133, 105),(228, 50),(251, 206)]
running = True
play_button = pygame.Surface((400,100))
play_button.fill((140,140,140))
pygame.draw.rect(play_button, (0,0,0), (0,0,400,100), width=2)
play_button.blit(font.render("Play Game", False, (0,0,0)), (100, 40))
while running:
    display.blit(bg, (0,0))
    for cloud in clouds:
        if cloud[0] > display.get_width():
            clouds.append((0, cloud[1]))
            clouds.remove(cloud)
        display.blit(cloud_img, cloud)
    clouds = [(x[0]+0.4, x[1]) for x in clouds]
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0,0))
    screen.blit(play_button, (screen.get_width()/2-200, screen.get_height()/2-50))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(screen.get_width()/2-200, screen.get_height()/2-50, play_button.get_width(), play_button.get_height()).collidepoint(pygame.mouse.get_pos()):
                play_game() 
    if pygame.Rect(screen.get_width()/2-200, screen.get_height()/2-50, play_button.get_width(), play_button.get_height()).collidepoint(pygame.mouse.get_pos()):
        play_button.fill((140,140,140))
        pygame.draw.rect(play_button, (0,0,0), (0,0,400,100), width=2)
        play_button.blit(font.render("Play Game", False, (255,255,255)), (100, 40))
    else:
        play_button.fill((140,140,140))
        pygame.draw.rect(play_button, (0,0,0), (0,0,400,100), width=2)
        play_button.blit(font.render("Play Game", False, (0,0,0)), (100, 40))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
        clock.tick(60)

