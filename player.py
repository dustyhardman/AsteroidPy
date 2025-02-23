import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(PLAYER_RADIUS, x, y)
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
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        pygame.draw.circle(
            screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), 2
        )  # DEBUG
