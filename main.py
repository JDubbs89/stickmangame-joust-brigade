import pygame,random,character,enemy,level,menu
pygame.init()

# Font used to display the score and other information
font = pygame.font.Font('freesansbold.ttf', 40)

# Creating and setting screen width and height, display caption
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Stickman")

# Setting the clock object and fps
clock = pygame.time.Clock() 
FPS = 60


player1 = character.Stickman(0)
player2 = character.Stickman(1)

allsprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
allsprites.add(player1,player2)

def main():
    running = True
    while running:
        
        # Update the display
          pygame.display.update()
          clock.tick(FPS)	