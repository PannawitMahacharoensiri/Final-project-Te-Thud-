import turtle
import random
import time

class Player:
    def __init__(self,color = "Blue"):
        self.grid_x = 5
        self.grid_y = 23
        self.color = color
        self.jump_fail = False

    def warp(self, after_x, after_y, grid):
        if 0 <= after_x < 12 and 0<= after_y < 23:
            grid[self.grid_y][self.grid_x] = 0
            self.grid_x,self.grid_y = after_x, after_y
            grid[self.grid_y][self.grid_x] = 2

    def move(self, dx, dy, grid):
        new_x = self.grid_x + dx
        new_y = self.grid_y + dy
        if 0 <= new_x < 12:
            if grid[new_y][new_x] == 0 :
                grid[self.grid_y][self.grid_x] = 0
                self.grid_x, self.grid_y = new_x, new_y
                grid[self.grid_y][self.grid_x] = 2

    def jump(self, grid):
        jump_height = 4
        if self.grid_y == 23 :
            for i in range(self.grid_y - jump_height, self.grid_y):
                if grid[i][self.grid_x] == 1:
                    self.jump_fail = True
            if not self.jump_fail :
                self.warp(self.grid_x, self.grid_y - jump_height, grid)
        else :
            if grid[self.grid_y+1][self.grid_x] ==1 :
                for i in range(self.grid_y - jump_height, self.grid_y):
                    if grid[i][self.grid_x] == 1:
                        self.jump_fail = True
                if not self.jump_fail:
                    self.warp(self.grid_x, self.grid_y - jump_height, grid)

class Obstacle:
    vertical_line = [[1],
                     [1],
                     [1],
                     [1]]
    short_line = [[1],
                  [1],
                  [1]]

    box = [[1, 1],
           [1, 1]]
    stand_left_l = [[0, 1],
                    [0, 1],
                    [1, 1]]
    stand_right_l = [[1, 0],
                     [1, 0],
                     [1, 1]]

    left_l = [[1, 0, 0],
              [1, 1, 1]]
    right_l = [[0, 0, 1],
               [1, 1, 1]]
    t = [[0, 1, 0],
         [1, 1, 1]]

    horizontal_line = [[1, 1, 1, 1]]

    def __init__(self,shape, grid_x = 5, grid_y = 5, state_fall = 0):
        self.shape = shape
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.height = len(self.shape)
        self.width = len(self.shape[0])
        self.state_fall = state_fall # 0: still falling, 1: stopped

    def print_piece(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1 :
                    grid[self.grid_y + y][self.grid_x + x] = 1

class Game:
    def __init__(self):
        # Grid 24 x 12
        self.size = 30
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.width = self.size * len(self.grid[0])
        self.height = self.size * (len(self.grid))
        self.gamedev = turtle.Turtle()
        self.obstacles = []
        self.game_over = False
        self.can_build = True
        self.screen = turtle.Screen()
        self.screen.setup(self.width, self.height)
        self.screen.title("Te-ThuD!!!!!!")
        self.player = Player()
        self.grid[self.player.grid_y][self.player.grid_x] = 2

        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkeypress(lambda: self.player.move(-1, 0, self.grid), "Left")
        self.screen.onkeypress(lambda: self.player.move(1, 0, self.grid), "Right")
        self.screen.onkey(lambda: self.player.jump(self.grid), "Up")

    def draw_grid(self):
        self.gamedev.clear()
        self.screen.tracer(0)
        self.gamedev.penup()
        self.gamedev.shape("square")
        for each_line in range(len(self.grid)) :
            for each_width in range(len(self.grid[0])) :
                screen_x = -110 + (each_width * 20)
                screen_y = 230 - (each_line * 20)
                """Use stamp"""
                self.gamedev.goto(screen_x, screen_y)
                if self.grid[each_line][each_width] == 1 :
                    self.gamedev.color("red")
                elif self.grid[each_line][each_width]  == 2 :
                    self.gamedev.color("blue")
                else :
                    self.gamedev.color("black")
                self.gamedev.stamp()
        self.screen.update()

    def add_shape(self,Object ):
        self.obstacles.append(Object)
        self.obstacles[0].print_piece(self.grid)

    def obstacle_can_fall(self, Object):
        for y in range(Object.height):
            for x in range(Object.width):
                if Object.shape[y][x] == 1:
                    grid_x = Object.grid_x + x
                    grid_y = Object.grid_y + y
                    self.grid[grid_y][grid_x] = 0
        can_fall = True
        for y in range(Object.height - 1, -1, -1):
            for x in range(Object.width):
                if Object.shape[y][x] == 1:
                    new_x = Object.grid_x + x
                    new_y = Object.grid_y + y + 1

                    if new_y >= 24 or self.grid[new_y][new_x] != 0:
                        can_fall = False
                        break
            if not can_fall:
                break

        for y in range(Object.height):
            for x in range(Object.width):
                if Object.shape[y][x] == 1:
                    grid_x = Object.grid_x + x
                    grid_y = Object.grid_y + y
                    self.grid[grid_y][grid_x] = 1
        return can_fall

    def player_fall(self):
        if self.player.grid_y + 1 <= 23:
            if self.grid[self.player.grid_y + 1][self.player.grid_x] == 0:
                self.grid[self.player.grid_y][self.player.grid_x] = 0
                self.player.grid_y += 1
                self.grid[self.player.grid_y][self.player.grid_x] = 2

    def obstacle_fall(self):
        for obstacle in self.obstacles:
            if self.obstacle_can_fall(obstacle):
                for y in range(obstacle.height):
                    for x in range(obstacle.width):
                        if obstacle.shape[y][x] == 1:
                            self.grid[obstacle.grid_y + y][obstacle.grid_x + x] = 0
                obstacle.grid_y += 1
                for y in range(obstacle.height):
                    for x in range(obstacle.width):
                        if obstacle.shape[y][x] == 1:
                            self.grid[obstacle.grid_y + y][obstacle.grid_x + x] = 1

                obstacle.state_fall = 1
            else:
                obstacle.state_fall = 0

    def check_collision(self):
        pos_x = self.player.grid_x
        pos_y = self.player.grid_y
        if pos_y > 0:
            if self.grid[pos_y - 1][pos_x] != 0:
                self.end_game()
        if self.player.jump_fail:
            self.end_game()

    def check_can_build(self):
        for obstacle in self.obstacles:
            if self.obstacle_can_fall(obstacle):
                self.can_build = False
                return
        self.can_build = True

    def random_block(self):
        shapes = {
            "Base1" : [Obstacle.vertical_line, Obstacle.short_line],
            "Base2" : [Obstacle.box, Obstacle.left_l, Obstacle.right_l],
            "Base3" : [Obstacle.left_l, Obstacle.right_l, Obstacle.t],
            "Base4" : [Obstacle.horizontal_line]
        }
        width_to_base = {
            1: ["Base1"],
            2: ["Base2"],
            3: ["Base2", "Base3"],
            4: ["Base2", "Base3", "Base4"]
        }

        start_row = 0
        start_col = random.randint(0, 11)
        place_row = len(self.grid) - 1

        for row in range(len(self.grid)):
            if self.grid[row][start_col] == 1:
                place_row = row - 1
                break
        max_width1 = 0
        max_width2 = 0
        for col in range(start_col, 11):
             if self.grid[place_row][col] != 1:
                 max_width1 += 1
             else:
                 break
        if place_row == 23 :
            max_width2 = 11-start_col
        else :
            currently_row = self.grid[place_row]
            for i in range(start_col,11):
                if currently_row[i] == 1 :
                    max_width2 += 1
                else :
                    break
        choose_width = min(max_width1, max_width2)
        if choose_width == 0 :
            choose_width = 1
        elif choose_width > 4 :
            choose_width = 4

        valid_bases = width_to_base[choose_width]
        chosen_base = random.choice(valid_bases)
        chosen_shape = random.choice(shapes[chosen_base])
        new_obstacle = Obstacle(chosen_shape, start_col,start_row)
        self.add_shape(new_obstacle)

    @staticmethod
    def draw_score(pen, score, location, font_size, color):
        font = ("Arial", font_size, "normal")
        pen.clear()
        pen.color(color)
        pen.hideturtle()
        pen.goto(location[0],location[1])
        pen.write("Time: {}".format(score), move=False, align="left", font=font)

    def end_game(self):
        self.game_over = True
        time.sleep(0.3)
        print("GAME OVER")

    def run(self):
        pen = turtle.Turtle()
        pen.penup()
        frame = 0
        while not self.game_over:
            self.draw_score(pen,frame,[-100, 250],24, "blue")
            self.check_can_build()
            if self.can_build :
                self.random_block()
            self.player_fall()
            self.check_collision()
            if frame % 2 == 0 :
                self.obstacle_fall()
            frame += 1
            self.draw_grid()
            self.screen.update()
            time.sleep(0.2)
        self.screen.clear()
        self.draw_score(pen, frame-1, [-90, 0], 40,"red")
        self.screen.bgcolor("pink")
        self.screen.mainloop()


if __name__ == "__main__":
    Demo = Game()
    Demo.run()