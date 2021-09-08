import pygame
import time
from Game_General_Info import Game_General_Info
from Game_Specific_Info import Game_Specific_Info

if __name__ == '__main__':

    pygame.init()
    ggi = Game_General_Info(600, 800, 10, 10, 12, pygame)
    bg = pygame.image.load("photos/grass_background.jpg")
    game_over = pygame.image.load("photos/game_over.jpg")
    start_screen = pygame.image.load("photos/main_game.jpg")

    pygame.display.set_caption('Snake Game new style')

    def gameLoop(ggi: Game_General_Info):
        gsi = Game_Specific_Info(ggi)
        go_on = ggi.begin_screen(pygame,start_screen)
        if go_on == 0:
            gsi.game_over = True
            gsi.game_close = False

        while not gsi.game_over:

            while gsi.game_close:
                ggi.screen.fill(ggi.black)
                ggi.screen.blit(game_over, (0, 0))
                ggi.Your_score(gsi.Length_of_snake - 1)
                pygame.display.update()
                time.sleep(1.3)
                gameLoop(ggi)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gsi.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        gsi.x1_change = -ggi.food_block
                        gsi.y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        gsi.x1_change = ggi.food_block
                        gsi.y1_change = 0
                    elif event.key == pygame.K_UP:
                        gsi.y1_change = -ggi.food_block
                        gsi.x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        gsi.y1_change = ggi.food_block
                        gsi.x1_change = 0

            gsi.check_in_screen(ggi)
            gsi.update_snake()
            ggi.screen.fill(ggi.black)
            ggi.screen.blit(bg, (0, 0))
            ggi.draw_food(gsi.food_x, gsi.food_y, pygame)

            ggi.our_snake( gsi.snake_List,pygame)
            ggi.Your_score(gsi.Length_of_snake - 1)
            pygame.display.update()
            gsi.food_pos(ggi)
            ggi.clock.tick(ggi.snake_speed)

        pygame.quit()
        quit()


    gameLoop(ggi)
