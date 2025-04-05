import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update the player
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if asteroid.is_colliding_with(player):
                print("Game over!")
                sys.exit()

        for shot in shots:
            if asteroid.collides_with(shot):
                shot.kill()
                asteroid.kill()

        # Draw Everything
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        # Limit framerate to 60 FPS and caculate delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
