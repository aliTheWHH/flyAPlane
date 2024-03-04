import pygame

pygame.init()

clock = pygame.time.Clock()

class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"img/exp{num}.png")
			img = pygame.transform.scale(img, (100, 100))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0

	def update(self):
		explosion_speed = 4
		#update explosion animation
		self.counter += 1

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#if the animation is complete, reset animation index
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()

explosion_group = pygame.sprite.Group()

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

SCORE = 0
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                  planerect.top -= 230

    towerrect = towerrect.move(-3, 0)
    if towerrect.right < -100:  
        towerrect.left = 1100

    towerrect2 = towerrect2.move(-3, 0)
    if towerrect2.right < -100:  
        towerrect2.left = 1100

    towerrect3 = towerrect3.move(-3, 0)
    if towerrect3.right < -100:  
        towerrect3.left = 1100

    planerect = planerect.move(0, 4)
    if planerect.bottom >= height:
          planerect.bottom = height
    if planerect.top <= 0:
          planerect.top = 0

    if planerect.colliderect(towerrect):
        pos = towerrect.topleft
        explosion = Explosion(pos[0], pos[1])
        explosion_group.add(explosion)

    if planerect.colliderect(towerrect2):
        pos = towerrect2.topleft
        explosion = Explosion(pos[0], pos[1])
        explosion_group.add(explosion)

    if planerect.colliderect(towerrect3):
        pos = towerrect3.topleft
        explosion = Explosion(pos[0], pos[1])
        explosion_group.add(explosion)
    
    win.blit(bg, (0,0))
    win.blit(plane, planerect)
    win.blit(tower, towerrect)
    win.blit(tower2, towerrect2)
    win.blit(tower3, towerrect3)

    explosion_group.draw(win)
    explosion_group.update()

    pygame.display.update()