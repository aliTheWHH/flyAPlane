import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.transform.scale(pygame.image.load(f"img/exp{num}.png"), (100, 100)) for num in range(1, 6)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0

    def update(self):
        explosion_speed = 4
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("c4.png"), (25, 30))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect.y += 5  # Adjust the speed as needed

# Screen dimensions
width, height = 1000, 700
win_size = width, height

win = pygame.display.set_mode(win_size)
pygame.display.set_caption("Fly a Plane")

# Load images
bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (width, height))
plane = pygame.transform.scale(pygame.image.load("plane.png"), (180, 90))
tower = pygame.image.load("tower.png")
tower2 = pygame.image.load("tower2.png")
tower3 = pygame.image.load("tower3.png")

# Initial positions
plane_topleft = 100, 0
tower_positions = [(600, 350), (1000, 300), (1400, 400)]

# Create sprites
plane_rect = plane.get_rect(topleft=plane_topleft)
tower_rects = [tower.get_rect(topleft=pos) for pos in tower_positions]
explosion_group = pygame.sprite.Group()
bomb_group = pygame.sprite.Group()

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bomb = Bomb(plane_rect.x + 50, plane_rect.y + 30)
                bomb_group.add(bomb)

    # Update positions
    plane_rect.x += 5  # Adjust the speed as needed

    for tower_rect in tower_rects:
        tower_rect.x -= 3
        if tower_rect.right < 0:
            tower_rect.left = width

    bomb_group.update()

    # Check for collisions with towers
    if any(plane_rect.colliderect(tower_rect) for tower_rect in tower_rects):
        pos = plane_rect.topleft
        explosion = Explosion(pos[0], pos[1])
        explosion_group.add(explosion)

    # Check for collisions with bombs
    if pygame.sprite.spritecollide(plane_rect, bomb_group, False):
        pos = plane_rect.topleft
        explosion = Explosion(pos[0], pos[1])
        explosion_group.add(explosion)
        bomb_group.empty()

    # Blit everything
    win.blit(bg, (0, 0))
    win.blit(plane, plane_rect)
    for tower_rect in tower_rects:
        win.blit(tower, tower_rect)

    bomb_group.draw(win)
    explosion_group.draw(win)
    explosion_group.update()

    pygame.display.update()

pygame.quit()
sys.exit()