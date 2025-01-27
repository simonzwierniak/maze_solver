import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable: # iterate over all the updatable objects
            obj.update(dt)

        screen.fill("black") # paint the screen in black
        
        for obj in drawable: # iterate over all the drawable objects
            obj.draw(screen)

        for asteroid in asteroids:
            if CircleShape.collision(asteroid, player) == True:
                print("Game over !")
                sys.exit()
            for shot in shots:
                if CircleShape.collision(asteroid, shot):
                    shot.kill()         # kill the missile
                    asteroid.split()    # split the asteroid

        pygame.display.flip() # refresh the display window
        dt = clock.tick(60) / 1000 # limit the framerate to  60 FPS 
          

if __name__ == "__main__":
    main()


    