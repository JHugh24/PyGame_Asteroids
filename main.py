import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0 #delta time

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    asteroidfield1 = AsteroidField()
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while 1 > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for item in asteroids:
            if player1.collision(item):
                print("Game over!")
                return
            for shot in shots:
                if shot.collision(item):
                    shot.kill()
                    item.split()

        screen.fill((0,0,0))
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        dt = fps_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
