import pygame
from game_objects import Player, Enemy, Collectible, Shield
from game_objects import WIDTH, HEIGHT  # reuse same constants
import random
from helpers import load_image

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Game")
clock = pygame.time.Clock()


ASSETS = {
    "player": load_image("images/ship.png", (60, 100)),
    "enemy": load_image("images/enemy.png", (60, 60)),
    "coin": load_image("images/coin.png", (30, 30)),
    # "shield": load_image("images/shield.png", (60, 60)),
}

# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
collectibles = pygame.sprite.Group()
player_group = pygame.sprite.GroupSingle()

# Create objects
player = Player(WIDTH // 2, HEIGHT - 50, ASSETS["player"], screen.get_rect())
shield = Shield(player.rect.centerx, player.rect.centery, radius=50)
enemy1 = Enemy(100, 150, ASSETS["enemy"], horizontal=True, speed=5)
enemy2 = Enemy(300, 300, ASSETS["enemy"], horizontal=False)
enemy3 = Enemy(50, 30, ASSETS["enemy"], horizontal=True)
enemy4 = Enemy(700, 30, ASSETS["enemy"], horizontal=False, speed=4)
enemy5 = Enemy(600, 50, ASSETS["enemy"], horizontal=False, speed=6)
enemy6 = Enemy(50, 400, ASSETS["enemy"], horizontal=True, speed=4)
enemy6 = Enemy(60, 550, ASSETS["enemy"], horizontal=True, speed=7)

for _ in range(5):
    collectibles.add(Collectible(ASSETS["coin"]))

enemies.add(enemy1, enemy2, enemy3, enemy4, enemy5, enemy6)
all_sprites.add(player, *enemies, *collectibles)
player_group.add(player)

# Game loop
running = True
score = 0
FPS = 60
no_collision_time = 60 * 5

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.update(keys)
    enemies.update()

    hits = pygame.sprite.spritecollide(
        player, collectibles, True, pygame.sprite.collide_mask
    )
    for _ in hits:
        score += 1
        new_coin = Collectible(ASSETS["coin"])
        collectibles.add(new_coin)
        all_sprites.add(new_coin)

    if no_collision_time <= 0 and player.check_collision_with_enemies(enemies):
        running = False

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    if no_collision_time > 0:
        no_collision_time -= 1
        shield.update(player)
        shield.draw(screen)

    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
