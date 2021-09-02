import pygame
import time
import random

if __name__ == '__main__':

    pygame.init()

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    dis_width = 800
    dis_height = 600
    bg = pygame.image.load("photos/room.jpeg")
    face_0 = pygame.image.load("photos/face_0.PNG")
    face_1 = pygame.image.load("photos/face_0.PNG")

    screen = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game new style')

    clock = pygame.time.Clock()
    toy_block = 15
    snake_block = 25
    snake_speed = 12

    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)


    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, white)
        screen.blit(value, [0, 0])

    def our_snake(snake_block, snake_list,state):
        if state == -1:
            pic = face_0
        else:
            pic = face_1
        len_list = len(snake_list)
        for x in range(len_list-1):
            pygame.draw.rect(screen, black, [snake_list[x][0], snake_list[x][1], snake_block, snake_block])

        screen.blit(pic, (snake_list[-1][0], snake_list[-1][1]))

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [dis_width / 6, dis_height / 3])


    def gameLoop():
        game_over = False
        game_close = False
        state = -1
        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close:
                screen.fill(black)
                screen.blit(bg,(0,0))
                message("You Lost! Press C-Play Again or Q-Quit", red)
                Your_score(Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -toy_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = toy_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -toy_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = toy_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            screen.fill(black)
            screen.blit(bg, (0, 0))
            pygame.draw.rect(screen, green, [foodx, foody, toy_block, toy_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List,state)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            state = state * (-1)

            if (foodx <= x1 <= foodx + float(toy_block)) and  (foody <= y1 <= foody + float(toy_block)):
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()


    gameLoop()
