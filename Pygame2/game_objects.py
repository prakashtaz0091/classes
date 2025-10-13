import pygame
import random
import math


# Import screen size constants from a central config or define here
WIDTH, HEIGHT = 800, 600


class Shield:
    def __init__(self, x, y, radius=40):
        self.x_pos = x
        self.y_pos = y
        self.radius = radius
        self.color = "green"
        self.rotation = 0

    def update(self, player):
        self.x_pos = player.rect.centerx
        self.y_pos = player.rect.centery
        self.rotation += 11

    def draw(self, screen):
        # Create a surface to draw the shield on
        size = self.radius * 2 + 10
        shield_surface = pygame.Surface((size, size), pygame.SRCALPHA)

        # Draw circle on the surface (centered)
        pygame.draw.circle(
            shield_surface,
            self.color,
            (size // 2, size // 2),
            self.radius,
            2,
            True,
            False,
            True,
            False,
        )

        # Rotate the surface
        rotated_surface = pygame.transform.rotate(
            shield_surface, self.rotation
        )

        # Get the rect and position it correctly
        rotated_rect = rotated_surface.get_rect(
            center=(self.x_pos, self.y_pos)
        )

        # Create a surface to draw the shield on
        size2 = self.radius * 2 + 20
        shield_surface2 = pygame.Surface((size2, size2), pygame.SRCALPHA)

        # Draw circle on the surface (centered)
        pygame.draw.circle(
            shield_surface2,
            "yellow",
            (size2 // 2, size2 // 2),
            self.radius + 10,
            3,
            False,
            True,
            False,
            True,
        )

        # Rotate the surface
        rotated_surface2 = pygame.transform.rotate(
            shield_surface2, self.rotation
        )

        # Get the rect and position it correctly
        rotated_rect2 = rotated_surface2.get_rect(
            center=(self.x_pos, self.y_pos)
        )

        # Blit to screen
        screen.blit(rotated_surface, rotated_rect)
        screen.blit(rotated_surface2, rotated_rect2)


# ----------------- ENEMY CLASS -----------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image, horizontal=True, speed=3):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.horizontal = horizontal
        self.speed = speed

    def update(self):
        """Move horizontally or vertically, bouncing off edges."""
        if self.horizontal:
            self.rect.x += self.speed
            if self.rect.right > WIDTH or self.rect.left < 0:
                self.speed *= -1
        else:
            self.rect.y += self.speed
            if self.rect.bottom > HEIGHT or self.rect.top < 0:
                self.speed *= -1


# ----------------- PLAYER CLASS -----------------
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image, screen_rect):
        """
        screen_rect: pass the screen.get_rect() from main.py
                     so Player doesn't depend on a global screen variable.
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5
        self.screen_rect = screen_rect

    def update(self, keys):
        """Handle keyboard movement (supports diagonal)."""
        dx = dy = 0
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed
        if keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_DOWN]:
            dy = self.speed

        self.rect.x += dx
        self.rect.y += dy
        self.rect.clamp_ip(self.screen_rect)

    def check_collision_with_enemies(self, enemy_group):
        """Mask-based collision with enemies."""
        return pygame.sprite.spritecollide(
            self, enemy_group, False, pygame.sprite.collide_mask
        )


# ----------------- COLLECTIBLE CLASS -----------------
class Collectible(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.respawn()

    def respawn(self):
        """Place collectible randomly on screen."""
        self.rect.center = (
            random.randint(20, WIDTH - 20),
            random.randint(20, HEIGHT - 20),
        )
