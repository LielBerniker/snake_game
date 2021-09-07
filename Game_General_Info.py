from UIElement import UIElement


class Game_General_Info:
    def __init__(self, height, width, toy_b, snake_b, snake_s, pygame):
        self.dis_height = height
        self.dis_width = width
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (213, 50, 80)
        self.pink = (255, 131, 250)
        self.toy_block = toy_b
        self.snake_block = snake_b
        self.snake_speed = snake_s
        self.toys_container = []
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        self.font_style = pygame.font.SysFont("bahnschrift", 25)

    def set_toys(self, *toys):
        for toy in toys:
            self.toys_container.append(toy)

    def Your_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, self.white)
        self.screen.blit(value, [0, 0])

    def message(self, msg):
        mesg = self.font_style.render(msg, True, self.red)
        self.screen.blit(mesg, [self.dis_width / 6, self.dis_height / 3])

    def draw_toy(self, toyx, toyy, rand_num):
        self.screen.blit(self.toys_container[rand_num], (toyx, toyy))

    def begin_screen(self, py_game):
        # create a ui element
        game_state = 1

        while True:
            if game_state == 1:
                game_state = self.title_screen(py_game)

            if game_state == 0:
                return 0
            else:
                return 1

    def title_screen(self,py_game):
        start_btn = UIElement(
            center_position=(400, 400),
            font_size=30,
            bg_rgb=self.black,
            text_rgb=self.white,
            text="Start Game",
            action=1,
        )
        quit_btn = UIElement(
            center_position=(400, 500),
            font_size=30,
            bg_rgb=self.black,
            text_rgb=self.white,
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

            for button in buttons:
                ui_action = button.update(py_game.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(self.screen)

            py_game.display.flip()


