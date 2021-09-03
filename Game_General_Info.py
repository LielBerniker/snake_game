class Game_General_Info:
    def __init__(self, height, width, toy_b, snake_b, snake_s):
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

    def set_toys(self, *toys):
        for toy in toys:
            self.toys_container.append(toy)
