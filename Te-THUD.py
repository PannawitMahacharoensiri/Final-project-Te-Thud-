"""
A Tetris-inspired video game where the goal is to dodge
falling blocks. If a block lands on you, the game is over.
"""

import turtle
import random
import time

class Player:
    """
    Responsible for constructing the player
    object and managing player movement.
    """
    def __init__(self,color = "#0f380f"):
        self.grid_x = 5
        self.grid_y = 23
        self.color = color
        self.jump_fail = False

    def warp(self, after_x, after_y, grid):
        """For change player to any position"""
        if 0 <= after_x < 12 and 0<= after_y < 23:
            grid[self.grid_y][self.grid_x] = 0
            self.grid_x,self.grid_y = after_x, after_y
            grid[self.grid_y][self.grid_x] = 2

    def move(self, dx, dy, grid):
        """Mimic real world movement, make player go left or right"""
        new_x = self.grid_x + dx
        new_y = self.grid_y + dy
        if 0 <= new_x < 12:
            if grid[new_y][new_x] == 0 :
                grid[self.grid_y][self.grid_x] = 0
                self.grid_x, self.grid_y = new_x, new_y
                grid[self.grid_y][self.grid_x] = 2

    def jump(self, grid):
        """Mimic Jump, make player go up 4 blocks"""
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
    """
    Serves as a blueprint for creating obstacle
    objects whenever they are instantiated.
    """
    vertical_line = [[1],
                     [1],
                     [1],
                     [1]]
    short_line = [[1],
                  [1],
                  [1]]
    tiny_line = [[1],
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
    rectangle = [[1, 1, 1],
                 [1, 1, 1]]


    horizontal_line = [[1, 1, 1, 1]]

    def __init__(self,shape, grid_x = 5, grid_y = 5, state_fall = 0):
        self.shape = shape
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.height = len(self.shape)
        self.width = len(self.shape[0])
        self.state_fall = state_fall

    def print_piece(self, grid):
        """Update the grid when it relates with obstacle"""
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1 :
                    grid[self.grid_y + y][self.grid_x + x] = 1

class Game:
    """
    The main class that handles the core game logic, including
    setting up the screen, processing user input, and coordinating
    interactions between objects from other classes.
    """
    def __init__(self):
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
        self.obstacles = []
        self.game_over = False
        self.can_build = True

        self.gamedev = turtle.Turtle()
        self.screen = turtle.Screen()
        self.player = Player()

        self.screen.setup(self.width, self.height)
        self.screen.bgcolor("#69992a")
        self.screen.title("Te-ThuD!!!!!!")
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkeypress(lambda: self.player.move(-1, 0, self.grid), "Left")
        self.screen.onkeypress(lambda: self.player.move(1, 0, self.grid), "Right")
        self.screen.onkey(lambda: self.player.jump(self.grid), "Up")

    def draw_grid(self):
        """Important method : use to change grid(list) to be in the picture format"""
        self.gamedev.clear()
        self.screen.tracer(0)
        self.gamedev.penup()
        self.gamedev.shape("square")
        for each_line in range(len(self.grid)) :
            for each_width in range(len(self.grid[0])) :
                screen_x = -110 + (each_width * 20)
                screen_y = 230 - (each_line * 20)
                self.gamedev.goto(screen_x, screen_y)
                if self.grid[each_line][each_width] == 1 :
                    self.gamedev.color("#306230")
                elif self.grid[each_line][each_width]  == 2 :
                    self.gamedev.color("#0f380f")
                else :
                    self.gamedev.color("#90be33")
                self.gamedev.stamp()
        self.screen.update()

    def add_shape(self,new_obstacle ):
        """method call to put object into list in class Game"""
        self.obstacles.append(new_obstacle)
        self.obstacles[0].print_piece(self.grid)

    def obstacle_can_fall(self, obstacle):
        """Important method : use to check can the obstacles fall"""
        for y in range(obstacle.height):
            for x in range(obstacle.width):
                if obstacle.shape[y][x] == 1:
                    grid_x = obstacle.grid_x + x
                    grid_y = obstacle.grid_y + y
                    self.grid[grid_y][grid_x] = 0
        can_fall = True
        for y in range(obstacle.height - 1, -1, -1):
            for x in range(obstacle.width):
                if obstacle.shape[y][x] == 1:
                    new_x = obstacle.grid_x + x
                    new_y = obstacle.grid_y + y + 1
                    if new_y >= 24 or self.grid[new_y][new_x] == 1:
                        can_fall = False
                        break
            if not can_fall:
                break
        for y in range(obstacle.height):
            for x in range(obstacle.width):
                if obstacle.shape[y][x] == 1:
                    grid_x = obstacle.grid_x + x
                    grid_y = obstacle.grid_y + y
                    self.grid[grid_y][grid_x] = 1
        return can_fall

    def player_fall(self):
        """check can the player fall, if they can update the player position in grid"""
        if self.player.grid_y + 1 <= 23:
            if self.grid[self.player.grid_y + 1][self.player.grid_x] == 0:
                self.grid[self.player.grid_y][self.player.grid_x] = 0
                self.player.grid_y += 1
                self.grid[self.player.grid_y][self.player.grid_x] = 2

    def obstacle_fall(self):
        """Update the Obstacle position if it can fall"""
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
        """Important method : Use to check and trigger game over"""
        pos_x = self.player.grid_x
        pos_y = self.player.grid_y
        if pos_y > 0:
            if self.grid[pos_y - 1][pos_x] != 0:
                self.end_game()
        if self.player.jump_fail:
            self.end_game()

    def check_can_build(self):
        """
        Important method : Use to check do they any obstacles still falling or
        row going to get clear or not that time they can't build new obstacle
        """
        for obstacle in self.obstacles:
            if self.obstacle_can_fall(obstacle):
                self.can_build = False
                return
        self.can_build = True

    def random_block(self):
        """Important method : Use to call class Obstacle ,calculate condition and build the block"""
        shapes = {
            "Base1" : [Obstacle.vertical_line, Obstacle.short_line,Obstacle.tiny_line],
            "Base2" : [Obstacle.box, Obstacle.box, Obstacle.stand_left_l, Obstacle.stand_right_l],
            "Base3" : [Obstacle.left_l, Obstacle.right_l, Obstacle.t, Obstacle.rectangle],
            "Base4" : [Obstacle.horizontal_line]
        }
        width_to_base = {
            1: ["Base1"],
            2: ["Base2"],
            3: ["Base2", "Base3", "Base3", "Base3"],
            4: ["Base2", "Base3", "Base3", "Base4", "Base4"]
        }
        start_row = 0
        start_col = random.randint(0, 11)
        place_row = len(self.grid) - 1
        for row in range(len(self.grid)):
            if self.grid[row][start_col] == 1:
                place_row = row - 1
                break
        if place_row >= 15 :
            max_width1 = 0
            max_width2 = 0
            for col in range(start_col, 11):
                if self.grid[place_row][col] != 1:
                    max_width1 += 1
                else:
                    break
            for col in range(0,start_col):
                if self.grid[place_row][col] != 1:
                    start_col -= 1
                    max_width1 += 1
                else :
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
        """use to draw the score why game still running"""
        font = ("Courier New", font_size, "normal")
        pen.clear()
        pen.color(color)
        pen.hideturtle()
        pen.goto(location[0],location[1])
        pen.write("Time: "+ f"{score}", move=False, align="left", font=font)

    @staticmethod
    def draw_game_over(pen, score, location):
        """use to draw the game over message"""
        font = ("Courier New", 50, "normal")
        font2 = ("Courier New", 30, "normal")
        pen.clear()
        pen.color("#948414")
        pen.hideturtle()
        pen.goto(location[0]+70 ,location[1]+70)
        pen.write("GAME", move=False, align="center", font=font)
        pen.goto(location[0] + 70, location[1] +20)
        pen.write("OVER", move=False, align="center", font=font)
        pen.color("#776b1b")
        pen.goto(location[0], location[1]-60)
        pen.write("Time: "+ f"{score}", move=False, align="left", font=font2)

    def end_game(self):
        """Important method : Stop the game if got trigger"""
        self.game_over = True
        time.sleep(0.3)
        print("GAME OVER")

    def delete_obstacle(self):
        """Important method : deleted the full row"""
        y = len(self.grid) - 1
        obstacles_to_keep = []
        while y >= 0:
            is_full = all(self.grid[y][x] == 1 for x in range(len(self.grid[0])))
            if is_full:
                for obstacle in self.obstacles:
                    if obstacle.grid_y <= y < obstacle.grid_y + obstacle.height:
                        pass
                    else:
                        obstacles_to_keep.append(obstacle)
                del self.grid[y]
                player_x, player_y = self.player.grid_x, self.player.grid_y
                if self.grid[player_y][player_x] == 2:
                    self.grid[player_y][player_x] = 0
                self.grid.insert(0, [0] * len(self.grid[0]))
            else:
                #the line not full go check next one
                y -= 1
        self.obstacles = obstacles_to_keep

    def run(self):
        """Important method : Run the Game"""

        self.grid[self.player.grid_y][self.player.grid_x] = 2
        pen = turtle.Turtle()
        pen.penup()
        frame = 0
        while not self.game_over:
            self.draw_score(pen,frame,[-120, 250],24, "#0f380f")
            self.check_can_build()
            if self.can_build :
                self.delete_obstacle()
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
        self.draw_game_over(pen,frame-1,[-120, 0])
        self.screen.bgcolor("#92be33")
        self.screen.mainloop()


if __name__ == "__main__":
    Demo = Game()
    Demo.run()
