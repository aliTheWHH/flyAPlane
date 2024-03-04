import pygame

pygame.init()

clock = pygame.time.Clock()

px = 0
py = 2

t1x = 600
t1y = 350

t2x = 1000
t2y = 300

t3x = 1400
t3y = 400

plane_topleft = x, y = 100, 0

move_up = 0

bg1 = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg1, (1000, 700))
plane1 = pygame.image.load("plane.png")
plane = pygame.transform.scale(plane1, (180, 90))
planerect = plane.get_rect()
planerect.topleft = plane_topleft
tower = pygame.image.load("tower.png")
tower2 = pygame.image.load("tower2.png")
tower3 = pygame.image.load("tower3.png")

towerrect = tower.get_rect()
towerrect.topleft = t1x,t1y

towerrect2 = tower2.get_rect()
towerrect2.topleft = t2x,t2y

towerrect3 = tower3.get_rect()
towerrect3.topleft = t3x,t3y

width = 1000
height = 700

win_size = width, height

win = pygame.display.set_mode(win_size)
pygame.display.set_caption("Fly a Plane")

run = True
while run:

    clock.tick(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    towerrect = towerrect.move(-3, 0)
    if towerrect.right < -100:  
        towerrect.left = 1100

    towerrect2 = towerrect2.move(-3, 0)
    if towerrect2.right < -100:  
        towerrect2.left = 1100

    towerrect3 = towerrect3.move(-3, 0)
    if towerrect3.right < -100:  
        towerrect3.left = 1100
    
    win.blit(bg, (0,0))
    win.blit(plane, planerect)
    win.blit(tower, towerrect)
    win.blit(tower2, towerrect2)
    win.blit(tower3, towerrect3)

    pygame.display.update()