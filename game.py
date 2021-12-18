'''the Whack-a-Mole game
'''

import pygame
import random
import time


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Whack-a-Mole')
    score = 0
    while True:
        x = random.randint(100, 500)
        y = random.randint(100, 500)
        mole = pygame.image.load('mole.png')
        screen.blit(mole, (x, y))
        pygame.display.update()
        time.sleep(0.5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if x < event.pos[0] < x + 100 and y < event.pos[1] < y + 100:
                        score -= 1
                        print(score)
                        time.sleep(0.5)
                        screen.fill((0, 0, 0))
                        pygame.display.update()
                    else:
                        score += 1
                        print(score)
                        time.sleep(0.5)
                        screen.fill((0, 0, 0))
                        pygame.display.update()



main()