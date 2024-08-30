import pygame, Utils, sys, math
from Animation import Animation

class Player:
    def __init__(self, anim):
        self.pos = (70,180)
        self.anim = anim
    def draw(self, display):
        display.blit(self.anim.img(), (self.pos[0]- camera_pos, self.pos[1]))
        self.anim.update()
        
class Interactable:
    def __init__(self, anim, func, draw, pos, light):
        self.func = func
        self.draw = draw
        self.anim = anim
        self.pos = pos
        self.light = light


class non_Interactable:
    def __init__(self, anim, draw, pos, light):
        self.draw = draw
        self.anim = anim
        self.pos = pos
        self.light = light

def draw_candle(anim, pos, light):
    display.blit(anim.img(), (pos[0]- camera_pos, pos[1]))
    lighting.blit(light, (((pos[0] - camera_pos)*w_ratio)-410,(pos[1]*h_ratio-440)), special_flags=pygame.BLEND_RGB_ADD)
    anim.update()

def draw_orb(anim, pos, light):
    display.blit(anim.img(), (pos[0]- camera_pos, pos[1]))
    lighting.blit(light, (((pos[0] - camera_pos)*w_ratio-100),(pos[1]*h_ratio-130)), special_flags=pygame.BLEND_RGB_ADD)
    anim.update()

def orb_interact():
    pass

def draw_important_potion(anim, pos, light):
    display.blit(anim.img(), (pos[0]- camera_pos, pos[1]))
    lighting.blit(light, (((pos[0] - camera_pos)*w_ratio)-5,(pos[1]*h_ratio)), special_flags=pygame.BLEND_RGB_ADD)
    anim.update()

def important_potion_interact():
    pass

def draw_caludron(anim, pos, light):
    display.blit(anim.img(), (pos[0]- camera_pos, pos[1]))
    lighting.blit(light, (((pos[0] - camera_pos)*w_ratio-100),(pos[1]*h_ratio-100)), special_flags=pygame.BLEND_RGB_ADD)
    anim.update()

def cauldron_interact():
    pass

def door_interact():
    pass

def draw_door(anim, pos, light):
    display.blit(anim.img(), (pos[0]- camera_pos, pos[1]))

def play_game():
    '''
    LOAD ROOM
    '''
    global camera_pos
    room_bg = Utils.load_image("assets/backgrounds/room.png")
    wizard_idle = Animation(Utils.load_images("assets/sprites/wizard/idle"), img_dur=6)
    wizard_walk_left = Animation(Utils.load_images("assets/sprites/wizard/walk left"), img_dur=4)
    wizard_walk_right = Animation(Utils.load_images("assets/sprites/wizard/walk right"), img_dur=4)
    cauldron_idle = Animation(Utils.load_images("assets/sprites/cauldron/idle"), img_dur=6)
    orb_idle = Animation(Utils.load_images("assets/sprites/orb/idle"), img_dur=8)
    important_potion_idle = Animation(Utils.load_images("assets/sprites/important potion/idle"), img_dur=6)
    door_img = Animation([Utils.load_image("assets/sprites/door.png")])
    player = Player(wizard_idle)
    '''
    LIGHTING
    '''
    candle_glow = pygame.Surface((1000,1000))
    for i in range(100):
        pygame.draw.circle(candle_glow, (i*251*0.01, i*164*0.01, i*50*0.01), (500,500), 500 - i * 5)
    orb_glow = pygame.Surface((400,400))
    for i in range(100):
        pygame.draw.circle(orb_glow, (i*50*0.01, i*104*0.01, i*251*0.01), (200,200), 120 - i * 1)
    potion_glow = pygame.Surface((200,200))
    for i in range(100):
        pygame.draw.circle(potion_glow, (i*250*0.01, i*104*0.01, i*200*0.01), (100,100), 60 - i * 1)
    cauldron_glow = pygame.Surface((400,400))
    for i in range(100):
        pygame.draw.circle(cauldron_glow, (i*250*0.01, i*164*0.01, i*50*0.01), (200,200), 200 - i * 2)
    window_light = pygame.Surface((1200,1200))
    for i in range(100):
        pygame.draw.circle(window_light, (i*220*0.01, i*255*0.01, i*220*0.01), (550,550), 550 - i * 5)
    

    '''
    OBJECTS
    '''
    candle = non_Interactable(Animation(Utils.load_images("assets/sprites/candle"), img_dur=6), draw_candle, (70, 140), candle_glow)
    candle2 = non_Interactable(Animation(Utils.load_images("assets/sprites/candle"), img_dur=6), draw_candle, (180, 120), candle_glow)
    candle3 = non_Interactable(Animation(Utils.load_images("assets/sprites/candle"), img_dur=6), draw_candle, (280, 140), candle_glow)
    orb = Interactable(orb_idle, orb_interact, draw_orb, (120,170), orb_glow)
    cauldron = Interactable(cauldron_idle, cauldron_interact, draw_caludron, (200,200), cauldron_glow)
    important_potion = Interactable(important_potion_idle, important_potion_interact, draw_important_potion, (170,157), potion_glow)
    for i in range(12):
        candle2.anim.update()
    door = Interactable(door_img, door_interact, draw_door, (330,165), None)
    non_interactables = [candle, candle2]
    interactables = [orb, important_potion, cauldron, door]
    '''
    MAIN LOOP
    '''
    running = True
    while running:
        '''
        DRAW
        '''

        interactions = []
        lighting.fill((10,10,10))
        display.fill((255,255,255))
        lighting.blit(window_light, (((225 - camera_pos)*w_ratio-100),(50*h_ratio-100)), special_flags=pygame.BLEND_RGB_ADD)
        display.blit(room_bg, (0-camera_pos,0))
        for non_interactable in non_interactables:
            non_interactable.draw(non_interactable.anim, non_interactable.pos, non_interactable.light)
        for interactable in interactables:
            interactable.draw(interactable.anim, interactable.pos, interactable.light)
            if(pygame.mask.from_surface(interactable.anim.img()).overlap_mask(pygame.mask.from_surface(player.anim.img()), (interactable.pos[0]-player.pos[0],0)).count()):
                interactions = [interactable]
        player.draw(display)
        screen.blit(pygame.transform.scale(display, screen.get_size()), (0,0))
        screen.blit(lighting, (0,0), special_flags=pygame.BLEND_RGB_MULT)
        for interactable in interactions:
            pygame.draw.rect(screen, (255,255,255), ((interactable.pos[0]-camera_pos)*w_ratio,interactable.pos[1]*h_ratio, 50, 50), 5)
            screen.blit(font.render("F", False, (255,255,255)),((interactable.pos[0]-camera_pos)*w_ratio + 15,interactable.pos[1]*h_ratio + 15))
        pygame.display.flip()

        '''
        ACTIONS
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
      
        keys = pygame.key.get_pressed()          
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_a]:
            player.anim = wizard_walk_left
            player.pos = (player.pos[0] - 1,player.pos[1])
        elif keys[pygame.K_d]:
            player.anim = wizard_walk_right
            player.pos = (player.pos[0] + 1,player.pos[1])
        elif player.anim != wizard_idle:
            player.anim = wizard_idle

        '''
        CAMERA MOVEMENT
        '''
        if abs(player.pos[0] - camera_pos - 100) > 50:
            camera_pos += math.floor((player.pos[0] - camera_pos - 100) * 0.01)
        clock.tick(60)

pygame.init()
'''
GAME WIDE DEFINITIONS
'''
clock = pygame.time.Clock()
display = pygame.Surface((320, 240))
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #scales 4:3 aspect ratio may adjust in future
lighting = pygame.Surface((screen.get_size()))
w_ratio = screen.get_width() / display.get_width()
h_ratio = screen.get_height() / display.get_height()
font = pygame.font.Font("assets/fonts/kongtext.ttf", 24)
camera_pos = -30

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

