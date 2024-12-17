import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroid, updateable, drawable)
    AsteroidField.containers = (updateable)


    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player(x, y)
    AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatables in updateable:
            updatables.update(dt)

        screen.fill((0,0,0))
        
        for drawables in drawable:
            drawables.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()