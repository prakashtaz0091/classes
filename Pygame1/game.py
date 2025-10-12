# Example file showing a basic pygame "game loop"
import pygame
from game_characters import Circle, PlayerCircle, Coin
from helpers import enemy_collides, check_coin_collisions

# pygame setup
pygame.init()

# Load a nice font: Impact (bold and dramatic), size 74
# If Impact isn't available, it uses the default font
try:
    font = pygame.font.SysFont("Arial", 50, bold=True)
except:
    font = pygame.font.Font(None, 50)  # Fallback to default Pygame font


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
game_over = False


circle1 = Circle(x_pos=10, y_pos=100)
circle2 = Circle(x_pos=10, y_pos=180, speed=15)
circle3 = Circle(x_pos=10, y_pos=250, speed=20)
circle4 = Circle(x_pos=10, y_pos=350, speed=25)


player = PlayerCircle(x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT - 40, speed=13)


# Render the text: "Game Over" in red, with anti-aliasing (True) for smoother edges
text = font.render("Game Over", True, (255, 0, 0))  # Red color
# Get text dimensions for centering
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))


coins = [Coin(screen) for _ in range(4)]


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    Circle.draw_all_circles_on_screen(screen)

    # Render coins
    Coin.draw_all_coins_on_screen(screen)

    # Render collected coins count
    # Text to display collected coin count
    coin_text = font.render(f"Coins: {player.collected_coins}", True, (255, 255, 255))
    coin_text_rect = coin_text.get_rect(center=(100, 50))
    screen.blit(coin_text, coin_text_rect)

    player.draw(screen)

    if not game_over:
        Circle.move_all_circles_on_screen(SCREEN_WIDTH)
        player.move(keys=pygame.key.get_pressed())

        check_coin_collisions(Coin.coins_list, player)

    else:
        # # Draw the text (blit it to the screen)
        screen.blit(text, text_rect)

    if enemy_collides(Circle.circle_list, player):
        game_over = True

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()
