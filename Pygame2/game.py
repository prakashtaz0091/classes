import pygame
from game_objects import Player, Enemy, Collectible, Shield
from game_objects import WIDTH, HEIGHT  # reuse same constants
import random
from helpers import load_image

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Game")
clock = pygame.time.Clock()


ASSETS = {
    "player": load_image("images/ship.png", (60, 100)),
    "enemy": load_image("images/enemy.png", (60, 60)),
    "coin": load_image("images/coin.png", (30, 30)),
    # "shield": load_image("images/shield.png", (60, 60)),
}


# Background music
pygame.mixer.music.load("music/Dark-Knight-chosic.com_.mp3")
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)

# SFX
coin_sound = pygame.mixer.Sound("music/coin_collect.wav")


# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
collectibles = pygame.sprite.Group()
player_group = pygame.sprite.Group()

# Create objects
player = Player(
    WIDTH // 3,
    HEIGHT - 50,
    ASSETS["player"],
    screen.get_rect(),
    up_key=pygame.K_UP,
    down_key=pygame.K_DOWN,
    left_key=pygame.K_LEFT,
    right_key=pygame.K_RIGHT,
    player_name="Rosse",
)
player2 = Player(
    WIDTH // 2 + 100,
    HEIGHT - 50,
    ASSETS["player"],
    screen.get_rect(),
    up_key=pygame.K_w,
    down_key=pygame.K_s,
    left_key=pygame.K_a,
    right_key=pygame.K_d,
    player_name="Prak1",
)
shield = Shield(player.rect.centerx, player.rect.centery, radius=50)
shield2 = Shield(player2.rect.centerx, player2.rect.centery, radius=50)
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
player_group.add(player, player2)
all_sprites.add(*player_group, *enemies, *collectibles)


font = pygame.font.Font(None, 36)

gameover_text = font.render("Game Over", True, (255, 0, 0))
player1_text = font.render(player.player_name, True, "blue")
player2_text = font.render(player2.player_name, True, "blue")

# Game loop
running = True
gameover = False
score_player1 = 0
score_player2 = 0
FPS = 60
no_collision_time = 60 * 5

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not gameover:
        keys = pygame.key.get_pressed()

        player.update(keys)
        player2.update(keys)

        enemies.update()

        coin_hits_player1 = pygame.sprite.spritecollide(
            player, collectibles, True, pygame.sprite.collide_mask
        )
        for _ in coin_hits_player1:
            score_player1 += 1
            coin_sound.play()
            new_coin = Collectible(ASSETS["coin"])
            collectibles.add(new_coin)
            all_sprites.add(new_coin)

        coin_hits_player2 = pygame.sprite.spritecollide(
            player2, collectibles, True, pygame.sprite.collide_mask
        )
        for _ in coin_hits_player2:
            score_player2 += 1
            coin_sound.play()
            new_coin = Collectible(ASSETS["coin"])
            collectibles.add(new_coin)
            all_sprites.add(new_coin)

        if no_collision_time <= 0 and (
            player.check_collision_with_enemies(enemies)
            or player2.check_collision_with_enemies(enemies)
        ):
            gameover = True

    # Draw objects ###########################################################
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    screen.blit(
        player1_text, (player.rect.centerx - 50, player.rect.centery + 50)
    )
    screen.blit(
        player2_text, (player2.rect.centerx - 50, player2.rect.centery + 50)
    )

    if no_collision_time > 0:
        no_collision_time -= 1
        shield.update(player)
        shield2.update(player2)
        shield.draw(screen)
        shield2.draw(screen)

    text_player1 = font.render(
        f"{player.player_name}: {score_player1}", True, (255, 255, 255)
    )
    screen.blit(text_player1, (10, 10))
    text_player2 = font.render(
        f"{player2.player_name}: {score_player2}", True, (255, 255, 255)
    )
    screen.blit(text_player2, (WIDTH - 200, 10))
    if gameover:
        screen.blit(gameover_text, (WIDTH // 2 - 50, HEIGHT // 2))

        winner = (
            player.player_name
            if score_player1 > score_player2
            else player2.player_name
        )
        winner_text = font.render(f"{winner} wins !", True, (255, 255, 255))
        screen.blit(winner_text, (WIDTH // 2 - 70, HEIGHT // 2 + 70))

    # Draw objects end ###########################################################

    pygame.display.flip()

pygame.quit()
