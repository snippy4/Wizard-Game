import pygame, os

def circle_surf(color, center, radius):
    shape_surf = pygame.Surface((radius*2, radius*2))
    pygame.draw.circle(shape_surf, color, (radius, radius), radius)
    shape_surf.set_colorkey((0,0,0))
    return shape_surf

def load_images(filepath):
    arr = []
    for img in sorted(os.listdir(filepath)):
        arr.append(pygame.image.load(filepath + '/' + img))
    return arr

def load_image(path):
    img = pygame.image.load(path)
    return img

def get_day_night_cycle_color(time_of_day: float):
    # Normalize time_of_day to be within [0, 1]
    time_of_day = time_of_day % 1.0

    if 0.0 <= time_of_day < 0.15:
        # Sunrise - From night (0, 0, 50) to daylight (255, 100, 50)
        ratio = time_of_day / 0.15
        r = int(0 + (255 - 0) * ratio)
        g = int(0 + (100 - 0) * ratio)
        b = int(50 + (50 - 50) * ratio)

    elif 0.15 <= time_of_day < 0.4:
        # Morning to Midday - From daylight (255, 100, 50) to bright daylight (200, 220, 255)
        ratio = (time_of_day - 0.15) / 0.25
        r = int(255 + (200 - 255) * ratio)
        g = int(100 + (220 - 100) * ratio)
        b = int(50 + (255 - 50) * ratio)

    elif 0.4 <= time_of_day < 0.6:
        # Midday - Bright bluish daylight (200, 220, 255)
        r, g, b = 200, 220, 255

    elif 0.6 <= time_of_day < 0.85:
        # Afternoon to Sunset - From bright daylight (200, 220, 255) to sunset (255, 100, 50)
        ratio = (time_of_day - 0.6) / 0.25
        r = int(200 + (255 - 200) * ratio)
        g = int(220 + (100 - 220) * ratio)
        b = int(255 + (50 - 255) * ratio)

    elif 0.85 <= time_of_day <= 0.9:
        # Sunset - From sunset (255, 100, 50) to night (0, 0, 50)
        ratio = (time_of_day - 0.85) / 0.05
        r = int(255 + (0 - 255) * ratio)
        g = int(100 + (0 - 100) * ratio)
        b = int(50 + (50 - 50) * ratio)

    elif 0.9 <= time_of_day <= 1.0:
        # Night at (0, 0, 50)
        r, g, b = 0, 0, 50
    

    return (r,g,b)