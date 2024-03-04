import pygame

pygame.init()
pygame.font.init()

px = 700
py = 70
bg1 = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg1, (1000, 700))
plane1 = pygame.image.load("plane.png")
plane = pygame.transform.scale(plane1, (180, 90))
planerect = plane.get_rect()
planerect.topleft = px,py
white = 255, 255, 255
black = 0,0,0

move = 200

font = pygame.font.SysFont("Arial", 40)
text = font.render("Press SPACE to Chill and watch a flying plane", True, black)
text2 = font.render("Press SPACE to play 9/11 flappy bird", True, black)
text3 = font.render("WORKING ON DROPPING BOMBS", True, black)

win = pygame.display.set_mode((1000, 700))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                planerect.top += move
            elif event.key == pygame.K_UP:
                planerect.top -= move
            if event.key == pygame.K_s:
                planerect.top += move
            elif event.key == pygame.K_w:
                planerect.top -= move
            elif event.key == pygame.K_SPACE:
                if planerect.top == 70:
                    run = False
                    import chill
                elif planerect.top == 270:
                    import flyingplane
                    run = False
                elif planerect.top == 470:
                    import chill
                    run = False

    if planerect.top <= 70:
        planerect.top = 70
    if planerect.top >=470:
        planerect.top = 470

    win.blit(bg, (0,0))
    win.blit(text, (0, 100))
    win.blit(text2, (0, 300))
    win.blit(text3, (0, 500))
    win.blit(plane, planerect)

    pygame.display.update()

pygame.quit()