import pygame
import random


class Circle:
    circle_list = []

    def __init__(self, x_pos=0, y_pos=0, speed=10, direction="right"):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed
        self.direction = direction
        self.color = "blue"
        self.radius = 40

        Circle.circle_list.append(self)

    def toggle_direction(self):
        if self.direction == "right":
            self.direction = "left"
        else:
            self.direction = "right"

    def change_direction(self, screen_width=0, screen_height=0):
        if self.x_pos >= screen_width or self.x_pos <= 0:
            self.toggle_direction()

    def move(self, screen_width=0, screen_height=0):
        self.change_direction(screen_width)
        if self.direction == "right":
            self.x_pos += self.speed
        else:
            self.x_pos -= self.speed

    @staticmethod
    def draw_all_circles_on_screen(screen):
        for circle in Circle.circle_list:
            pygame.draw.circle(
                screen, circle.color, (circle.x_pos, circle.y_pos), circle.radius
            )

    @staticmethod
    def move_all_circles_on_screen(screen_width=0, screen_height=0):
        for circle in Circle.circle_list:
            circle.move(screen_width, screen_height)


class PlayerCircle:
    def __init__(self, x_pos=0, y_pos=0, speed=10):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed
        self.color = "green"
        self.radius = 40
        self.collected_coins = 0

    def draw(self, screen):
        self.screen = screen
        pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def move(self, keys):
        sc_height = (
            self.screen.get_height()
        )  # x pos, must be greater than 0 and less than screen height
        sc_width = (
            self.screen.get_width()
        )  # x pos, must be greater than 0 and less than screen width

        if keys[pygame.K_LEFT]:
            if self.x_pos >= 0:
                self.x_pos -= self.speed
        elif keys[pygame.K_RIGHT]:
            if self.x_pos <= sc_width:
                self.x_pos += self.speed

        if keys[pygame.K_UP]:
            if self.y_pos >= 0:
                self.y_pos -= self.speed
        elif keys[pygame.K_DOWN]:
            if self.y_pos <= sc_height:
                self.y_pos += self.speed


class Coin:
    coins_list = []

    def __init__(self, screen, radius=20, color="yellow"):
        self.screen = screen
        self.radius = radius
        self.color = color

        self.x_pos = random.randint(20, screen.get_width() - 20)
        self.y_pos = random.randint(20, screen.get_height() - 20)

        Coin.coins_list.append(self)

    def destroy(self):
        Coin.coins_list.remove(self)
        if len(Coin.coins_list) < 4:
            Coin.coins_list.append(Coin(self.screen))

    @staticmethod
    def draw_all_coins_on_screen(screen):
        for coin in Coin.coins_list:
            pygame.draw.circle(
                screen, coin.color, (coin.x_pos, coin.y_pos), coin.radius
            )
