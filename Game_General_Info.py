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

    def message(self,msg):
        mesg = self.font_style.render(msg, True,self.red)
        self.screen.blit(mesg, [self.dis_width / 6, self.dis_height / 3])

    def draw_toy(self,toyx, toyy, rand_num):
        self.screen.blit(self.toys_container[rand_num], (toyx, toyy))
