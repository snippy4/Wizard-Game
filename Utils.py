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

    if 0.0 <= time_of_day < 0.25:
        # Dawn - From night (0, 0, 50) to sunrise (255, 100, 50)
        ratio = time_of_day / 0.25
        r = int(0 + (255 - 0) * ratio)
        g = int(0 + (100 - 0) * ratio)
        b = int(50 + (50 - 50) * ratio)

    elif 0.25 <= time_of_day < 0.5:
        # Morning - From sunrise (255, 100, 50) to midday (135, 206, 235)
        ratio = (time_of_day - 0.25) / 0.25
        r = int(255 + (135 - 255) * ratio)
        g = int(100 + (206 - 100) * ratio)
        b = int(50 + (235 - 50) * ratio)

    elif 0.5 <= time_of_day < 0.75:
        # Afternoon - From midday (135, 206, 235) to sunset (255, 100, 50)
        ratio = (time_of_day - 0.5) / 0.25
        r = int(135 + (255 - 135) * ratio)
        g = int(206 + (100 - 206) * ratio)
        b = int(235 + (50 - 235) * ratio)

    elif 0.75 <= time_of_day <= 1.0:
        # Evening - From sunset (255, 100, 50) to night (0, 0, 50)
        ratio = (time_of_day - 0.75) / 0.25
        r = int(255 + (0 - 255) * ratio)
        g = int(100 + (0 - 100) * ratio)
        b = int(50 + (50 - 50) * ratio)

    return (r, g, b)