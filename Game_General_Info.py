from UIElement import UIElement
import timeit


class Game_General_Info:
    def __init__(self, height, width, food_b, snake_b, snake_s, pygame):
        self.dis_height = height
        self.dis_width = width
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red1 = (238, 44, 44)
        self.red2 = (178, 34, 34)
        self.cyan3 = (16,78,139)
        self.state = -1
        self.dis = pygame.display.set_mode((width, height))
        self.count_time = timeit.default_timer()
        self.food_block = food_b
        self.snake_block = snake_b
        self.snake_speed = snake_s
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        self.font_style = pygame.font.SysFont("bahnschrift", 25)

    def Your_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, self.white)
        self.screen.blit(value, [0, 0])

    def message(self, msg):
        mesg = self.font_style.render(msg, True, self.red2)
        self.screen.blit(mesg, [self.dis_width / 6, self.dis_height / 3])

    def draw_food(self, foodx, foody, pygame):
        current_time = timeit.default_timer()
        if current_time - self.count_time > 0.4:
            self.count_time = current_time
            self.state = self.state * (-1)
        if self.state == -1:
            color_temp = self.red1
        else:
            color_temp = self.red2
        pygame.draw.rect(self.dis, color_temp, [foodx, foody, self.food_block, self.food_block])

    def our_snake(self, snake_list, pygame):
        i = 0
        for x in snake_list:
            if i % 2 == 0:
                color_temp = self.black
            else:
                color_temp = self.cyan3
            i = i+1
            pygame.draw.rect(self.dis, color_temp, [x[0], x[1], self.snake_block, self.snake_block])

    def begin_screen(self, py_game,start_screen):
        # create a ui element
        game_state = 1

        while True:
            if game_state == 1:
                game_state = self.title_screen(py_game,start_screen)

            if game_state == 0:
                return 0
            else:
                return 1

    def title_screen(self, py_game,start_screen):
        start_btn = UIElement(
            center_position=(400, 400),
            font_size=30,
            bg_rgb=self.black,
            text_rgb=self.black,
            text="Start Game",
            action=1,
        )
        quit_btn = UIElement(
            center_position=(400, 500),
            font_size=30,
            bg_rgb=self.black,
            text_rgb=self.black,
            text="Quit",
            action=0,
        )

        buttons = [start_btn, quit_btn]

        while True:
            mouse_up = False
            for event in py_game.event.get():
                if event.type == py_game.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(self.black)
            self.screen.blit(start_screen, (0, 0))

            for button in buttons:
                ui_action = button.update(py_game.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(self.screen)

            py_game.display.flip()
