import time
import pygame
seconds = time.time()


def do():
    print("Seconds since epoch =", seconds)
    seconds = 1589561509.4362562
    local_time = time.ctime(seconds)
    print("Local time:", local_time)
    print("This is printed immediately.")
    time.sleep(3)
    print("This is printed after 3 seconds.")
    pygame.init()
    white = (255, 255, 255)
    X = 400
    Y = 400
    display_surface = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('Image')
    image = pygame.image.load(r'C:\Users\Kimi Wan\Pictures\geek.jpg')
    while True:
        display_surface.fill(white)
        display_surface.blit(image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
"""
user_input = input("Enter a group of numbers: ")
try:
    pass
except ValueError:
    print("There was an error")
else:
    my_list = user_input.split(" ")
print(my_list)
"""
dice = randint(1,7)
if dice == 1:
    pygame.image.load("Dice 1.png")
elif dice == 2:
    pygame.image.load("Dice 2.png")
elif dice == 3:
    pygame.image.load("Dice 3.png")
elif dice == 4:
        pygame.image.load("Dice 4.png")
elif dice == 5:
    pygame.image.load("Dice 5.png")
else:
    pygame.image.load("Dice 6.png")