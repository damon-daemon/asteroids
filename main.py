import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
from shot import Shot
from sys import exit as system

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game = pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    shots_group = []
    player = Player(SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, shots_group)
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for shot in shots_group:
            shot.update(dt)
            shot.draw(screen)
        for update in updatable:
            update.update(dt)
        for draw in drawable:
            draw.draw(screen)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over!")
                system.exit()
        player.update(dt)                
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)

if __name__ == "__main__":
    main()
