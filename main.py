import pygame
import time
import random
import timeit
from Game_General_Info import Game_General_Info
from Game_Specific_Info import Game_Specific_Info

if __name__ == '__main__':

    pygame.init()
    ggi = Game_General_Info(600, 800, 20, 40, 12,pygame)
    bg = pygame.image.load("photos/room.jpeg")
    face_0 = pygame.image.load("photos/face_0.PNG")
    face_1 = pygame.image.load("photos/face_1.PNG")
    circle = pygame.image.load("photos/circle_toy.PNG")
    horse = pygame.image.load("photos/horse.PNG")
    ball = pygame.image.load("photos/pool_ball.PNG")
    wood = pygame.image.load("photos/wood.PNG")
    ggi.set_toys(circle, horse, ball, wood)
    pygame.display.set_caption('Snake Game new style')

    def our_snake(snake_block, snake_list, state):
        if state == -1:
            pic = face_0
        else:
            pic = face_1
        len_list = len(snake_list)
        for x in range(len_list - 1):
            pygame.draw.rect(ggi.screen, ggi.pink, [snake_list[x][0], snake_list[x][1], snake_block, snake_block])

        ggi.screen.blit(pic, (snake_list[-1][0], snake_list[-1][1]))

    def gameLoop(ggi: Game_General_Info):
        gsi = Game_Specific_Info(ggi)

        while not gsi.game_over:

            while gsi.game_close:
                ggi.screen.fill(ggi.black)
                ggi.screen.blit(bg, (0, 0))
                ggi.message("You Lost! Press C-Play Again or Q-Quit")
                ggi.Your_score(gsi.Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gsi.game_over = True
                            gsi.game_close = False
                        if event.key == pygame.K_c:
                            gameLoop(ggi)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gsi.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        gsi.x1_change = -ggi.toy_block
                        gsi.y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        gsi.x1_change = ggi.toy_block
                        gsi.y1_change = 0
                    elif event.key == pygame.K_UP:
                        gsi.y1_change = -ggi.toy_block
                        gsi.x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        gsi.y1_change = ggi.toy_block
                        gsi.x1_change = 0

            gsi.check_in_screen(ggi)
            gsi.update_snake()
            ggi.screen.fill(ggi.black)
            ggi.screen.blit(bg, (0, 0))
            ggi.draw_toy(gsi.toy_x, gsi.toy_y, gsi.rand_num)

            our_snake(ggi.snake_block, gsi.snake_List, gsi.state)
            ggi.Your_score(gsi.Length_of_snake - 1)
            pygame.display.update()
            gsi.change_state()
            gsi.toy_pos(ggi)
            ggi.clock.tick(ggi.snake_speed)

        pygame.quit()
        quit()


    gameLoop(ggi)
