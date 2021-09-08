
import random
import Game_General_Info


class Game_Specific_Info:
    def __init__(self, ggi: Game_General_Info):
        self.game_over = False
        self.game_close = False
        self.x1 = ggi.dis_width / 2
        self.y1 = ggi.dis_height / 2
        self.x1_change = 0
        self.y1_change = 0
        self.snake_List = []
        self.Length_of_snake = 1
        self.rand_num = 0
        self.food_x = self.round_position_x(ggi.dis_width, ggi.snake_block)
        self.food_y = self.round_position_y(ggi.dis_height, ggi.snake_block)

    @staticmethod
    def round_position_x(dis_width, snake_b):
        return round(random.randrange(0, dis_width - snake_b) / 10.0) * 10.0

    @staticmethod
    def round_position_y(dis_height, snake_b):
        return round(random.randrange(0, dis_height - snake_b) / 10.0) * 10.0

    def collect_food(self, ggi: Game_General_Info):
        if (self.food_x == self.x1 ) and (self.food_y == self.y1):
            return True
        return False

    def food_pos(self, ggi: Game_General_Info):
        if self.collect_food(ggi):
            self.food_x = self.round_position_x(ggi.dis_width, ggi.snake_block)
            self.food_y = self.round_position_y(ggi.dis_height, ggi.snake_block)
            self.Length_of_snake += 1

    def check_in_screen(self, ggi: Game_General_Info):
        if self.x1 >= ggi.dis_width or self.x1 < 0 or self.y1 >= ggi.dis_height or self.y1 < 0:
            self.game_close = True

    def update_snake(self):
        self.x1 += self.x1_change
        self.y1 += self.y1_change
        snake_Head = [self.x1, self.y1]
        self.snake_List.append(snake_Head)
        if len(self.snake_List) > self.Length_of_snake:
            del self.snake_List[0]

        for x in self.snake_List[:-1]:
            if x == snake_Head:
                self.game_close = True

