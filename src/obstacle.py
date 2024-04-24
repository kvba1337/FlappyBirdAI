import pygame
import random
import src.config as config

class Obstacle:
    def __init__(self, x, y, width, height):
        self.position = pygame.Rect(x, y, width, height)
        self.color = config.BLACK

class Obstacles:
    def __init__(self):
        self.obstacles = []

    def get_obstacles(self):
        return self.obstacles

    def generate_obstacles(self):
        if len(self.obstacles) == 0 or self.obstacles[-1].position.x <= config.GAME_HEIGHT - 300:
            if len(self.obstacles) > 4:
                self.remove()
            
            gap_height = random.randint(config.GAME_HEIGHT - 500, config.GAME_HEIGHT - 200)

            top_obstacle = Obstacle(config.GAME_WIDTH, 0, config.OBSTACLE_WIDTH, gap_height)
            bottom_obstacle = Obstacle(config.GAME_WIDTH, gap_height + config.GAP_HEIGHT_SIZE, config.OBSTACLE_WIDTH, config.GAME_HEIGHT - gap_height - config.GAP_HEIGHT_SIZE)

            self.obstacles.extend([top_obstacle, bottom_obstacle])

    def update(self):
        for obstacle in self.obstacles:
            obstacle.position.x -= config.GAME_SPEED

    def remove(self):
        self.obstacles.pop(0)

    def draw(self, window):
        for obstacle in self.obstacles:
            pygame.draw.rect(window, obstacle.color, obstacle.position)

    def clear(self):
        self.obstacles.clear()