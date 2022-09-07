import pygame
import math
import os

os.environ['SDL_VIDEO_CENTERED']='1'

#pygame configurations
width,height = 1920, 1080

fps = 30
pygame.display.set_caption("Fourier Series Tutorial")
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#colours
white =(255, 255, 255)
gray = (160, 160, 160)
black =(0, 0, 0)
crimson = (230 , 20, 32)

# screen.fill()
N = 1
time = 0
radius = 0
pos_x = 240
pos_y = 480
wave_list = []
offset = 300

Iterations = 5

run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    x = pos_x
    y = pos_y
    for i in range(Iterations):
        old_x, old_y = x, y

        N = i * 2 + 1 # 1,3,5,7,9,......
        radius = 150 * (4/(N * math.pi))
        x += int(radius * math.cos(N * time))
        y += int(radius * math.sin(N * time))

        pygame.draw.circle(screen, white, (old_x, old_y), int(radius), 2)
        pygame.draw.line(screen, gray, (old_x, old_y), (x,y), 3)
        pygame.draw.circle(screen, crimson, (x,y), 5)
    wave_list.insert(0, y)
    if len(wave_list) > 1000:
        wave_list.pop()

    pygame.draw.line(screen, white, (x, y), (pos_x + offset, wave_list[0]), 3)
    
    for index in range(len(wave_list)):
        pygame.draw.circle(screen, white, (index + pos_x + offset, wave_list[index]), 3)
        time += 0.001
    pygame.display.update()
    
pygame.quit()

