import pygame
import time
import random
import timeit
from Game_General_Info import Game_General_Info
from Game_Specific_Info import Game_Specific_Info

if __name__ == '__main__':

    pygame.init()
    ggi = Game_General_Info(600, 800, 20, 40, 12)
    bg = pygame.image.load("photos/room.jpeg")
    face_0 = pygame.image.load("photos/face_0.PNG")
    face_1 = pygame.image.load("photos/face_1.PNG")
    circle = pygame.image.load("photos/circle_toy.PNG")
    horse = pygame.image.load("photos/horse.PNG")
    ball = pygame.image.load("photos/pool_ball.PNG")
    wood = pygame.image.load("photos/wood.PNG")
    ggi.set_toys(circle, horse, ball, wood)

    screen = pygame.display.set_mode((ggi.dis_width, ggi.dis_height))
    pygame.display.set_caption('Snake Game new style')

    clock = pygame.time.Clock()

    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)


    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, ggi.white)
        screen.blit(value, [0, 0])


    def our_snake(snake_block, snake_list, state):
        if state == -1:
            pic = face_0
        else:
            pic = face_1
        len_list = len(snake_list)
        for x in range(len_list - 1):
            pygame.draw.rect(screen, ggi.pink, [snake_list[x][0], snake_list[x][1], snake_block, snake_block])

        screen.blit(pic, (snake_list[-1][0], snake_list[-1][1]))


    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [ggi.dis_width / 6, ggi.dis_height / 3])


    def draw_toy(toyx, toyy, rand_num):
        screen.blit(ggi.toys_container[rand_num], (toyx, toyy))


    def gameLoop(ggi: Game_General_Info):
        gsi = Game_Specific_Info(ggi)

        while not gsi.game_over:

            while gsi.game_close:
                screen.fill(ggi.black)
                screen.blit(bg, (0, 0))
                message("You Lost! Press C-Play Again or Q-Quit", ggi.red)
                Your_score(gsi.Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gsi.game_over = True
                            gsi.game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

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
            screen.fill(ggi.black)
            screen.blit(bg, (0, 0))
            draw_toy(gsi.toy_x, gsi.toy_y, gsi.rand_num)

            our_snake(ggi.snake_block, gsi.snake_List, gsi.state)
            Your_score(gsi.Length_of_snake - 1)
            pygame.display.update()
            gsi.change_state()
            gsi.toy_pos(ggi)
            clock.tick(ggi.snake_speed)

        pygame.quit()
        quit()


    gameLoop(ggi)
