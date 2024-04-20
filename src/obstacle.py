import pygame
import random
import src.myconstants as myconstants

class Obstacle:
    def __init__(self, x, y, width, height):
        self.position = pygame.Rect(x, y, width, height)
        self.color = myconstants.BLACK

class Obstacles:
    def __init__(self):
        self.obstacles = []
        self.counter = 0

    def get_obstacles(self):
        return self.obstacles

    def generate_obstacles(self, window, mode):
        if len(self.obstacles) == 0 or self.obstacles[-1].position.x <= window.width - 300:
            if len(self.obstacles) > 4:
                self.remove()
            
            if mode == "random":
                gap_height = random.randint(window.height - 500, window.height - 200)
            elif mode == "static":
                if self.counter == len(myconstants.GAP_HEIGHT_LIST):
                    self.counter = 0
                gap_height = myconstants.GAP_HEIGHT_LIST[self.counter]
                self.counter += 1

            top_obstacle = Obstacle(window.width, 0, myconstants.OBSTACLE_WIDTH, gap_height)
            bottom_obstacle = Obstacle(window.width, gap_height + myconstants.GAP_HEIGHT_SIZE, myconstants.OBSTACLE_WIDTH, window.height - gap_height - myconstants.GAP_HEIGHT_SIZE)
            self.obstacles.extend([top_obstacle, bottom_obstacle])

    def update(self, background):
        for obstacle in self.obstacles:
            obstacle.position.x -= background.speed

    def remove(self):
        self.obstacles.pop(0)

    def draw(self, window):
        for obstacle in self.obstacles:
            pygame.draw.rect(window, obstacle.color, obstacle.position)

    def clear(self):
        self.obstacles.clear()