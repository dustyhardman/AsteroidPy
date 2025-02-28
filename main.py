import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update the player
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if player.is_colliding_with(asteroid):
                print("Game over!")
                import sys

                sys.exit()

        # Draw Everything
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        # Limit framerate to 60 FPS and caculate delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
