import pygame


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
