import random

import pygame
import sys
from pygame.locals import *


pygame.init()

DISPLAY_SURF = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Dice Rolling Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,  255, 0)
BLUE = (0, 0, 255)
DISPLAY_SURF.fill(BLUE)

# x-axis = screen length(x-axis) - shape length(x-axis) / 2
# y-axis = screen length(y-axis) - shape length(y-axis) / 2
# The first number if for the x-axis and the second number is the y-axis
# The third and fourth numbers are for the length and width


def drawing_1():
    # The Base rect
    pygame.draw.rect(DISPLAY_SURF, WHITE, (100, 100, 300, 300))
    # The Middle
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (210, 210, 80, 80))


def drawing_2():
    # The Base for the Dice
    pygame.draw.rect(DISPLAY_SURF, WHITE, (100, 100, 300, 300))
    # Top Left corner
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (153, 153, 40, 40))
    # Bottom Right corner
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (307, 307, 40, 40))


def drawing_3():
    # The Base rect
    pygame.draw.rect(DISPLAY_SURF, WHITE, (100, 100, 300, 300))
    # Middle Left corner
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (153, 230, 40, 40))
    # Middle
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (230, 230, 40, 40))
    # Middle Right corner
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (307, 230, 40, 40))


def drawing_4():
    # Base rect
    pygame.draw.rect(DISPLAY_SURF, WHITE, (100, 100, 300, 300))
    # Top Left Corner
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (153, 153, 40, 40))
    # Top Right Corner
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (307, 153, 40, 40))
    # Bottom Left Corner
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (153, 307, 40, 40))
    # Bottom Right Corner
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (307, 307, 40, 40))


def drawing_5():
    # Base rect
    pygame.draw.rect(DISPLAY_SURF, WHITE, (100, 100, 300, 300))
    # Top Left corner
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (153, 153, 40, 40))
    # Top Right corner
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (307, 153, 40, 40))
    # Middle
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (230, 230, 40, 40))
    # Bottom Left corner
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (153, 307, 40, 40))
    # Bottom Right corner
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (307, 307, 40, 40))


def drawing_6():
    # Base rect
    pygame.draw.rect(DISPLAY_SURF, WHITE, (100, 100, 300, 300))
    # 1/4 of Top Right
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (150, 140, 40, 40))
    # Top Middle
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (230, 140, 40, 40))
    # 3/4 of Top Left
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (307, 140, 40, 40))
    # 1/4 of Bottom Right
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (150, 300, 40, 40))
    # Bottom Middle
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (230, 300, 40, 40))
    # 3/4 Bottom Left
    pygame.draw.ellipse(DISPLAY_SURF, BLACK, (307, 300, 40, 40))


def main():
    # user_input = int(input("How much dice do you want to individually roll? "))
    # while user_input > 0:
    dice = random.randint(1, 7)
    if dice == 1:
        drawing_1()
    elif dice == 2:
        drawing_2()
    elif dice == 3:
        drawing_3()
    elif dice == 4:
        drawing_4()
    elif dice == 5:
        drawing_5()
    else:
        drawing_6()


# main()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            # Using the KEYDOWN function, you can control pygame with any key you want!!!
        elif event.type == pygame.KEYDOWN:
            main()

    pygame.display.update()
