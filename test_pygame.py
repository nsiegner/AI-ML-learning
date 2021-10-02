import pygame


#initializing pygame
pygame.init()

all_sprites = pygame.sprite.Group()
size = WIDTH , HEIGHT = 640, 480
GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


player = Player()
all_sprites.add(player)
#initializing a clock for window refreshment
clock = pygame.time.Clock()



#declaring screen

screen = pygame.display.set_mode(size)
#setting the heading to the screen
pygame.display.set_caption("Test_Game")

#declaring colors
WHITE = (255, 255, 255)
#introducing the variable to keep track if the game is still running
game_running = True

#
pressed_key = None
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        elif event.type == pygame.K_RIGHT:
            pressed_key = "right"
        elif event.type == pygame.K_LEFT:
            pressed_key = "left"
        elif event.type == pygame.K_UP:
            pressed_key = "up"
        elif event.type == pygame.K_DOWN:
            pressed_key = "down"

    #chageing window color
    #screen.fill(WHITE)

    #refreshing the window
    pygame.display.flip()

    #setting fps
    clock.tick(60)


    all_sprites.update()
    all_sprites.draw(screen)

pygame.quit()
