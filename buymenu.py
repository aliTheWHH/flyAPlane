import pygame

win = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Plane Buy Menu")

bg1 = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg1, (1000, 700))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.blit(bg, (0,0))

    pygame.display.update()

    