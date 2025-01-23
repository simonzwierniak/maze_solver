import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
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

        pygame.display.flip() # refresh the display window
        dt = clock.tick(60) / 1000 # limit the framerate to  60 FPS 
          

if __name__ == "__main__":
    main()


    