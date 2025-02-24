import pygame

from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update the player
        player.update(dt)

        # Draw Everything
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # Limit framerate to 60 FPS and caculate delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
