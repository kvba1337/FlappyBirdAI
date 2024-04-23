import pygame

class Window:
    def __init__(self, window_width, window_height):
        self.width = window_width
        self.height = window_height
        self.display_surface = pygame.display.set_mode((self.width, self.height), vsync=1)