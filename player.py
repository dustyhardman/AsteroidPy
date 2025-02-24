import pygame

from circleshape import CircleShape
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        print(f"Initialized Player Position: {self.position}")  # DEBUG

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        pygame.draw.circle(
            screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), 2
        )  # DEBUG

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED + dt
        print(f"Rotation updated to: {self.rotation}")  # DEBUG

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
