import pygame
from pygame.locals import *
import src.config as config
from src.hero import Hero
from src.obstacle import Obstacles
from src.window import Window
from src.overlay import print_score, print_game_over, print_paused

class Game:
    def __init__(self):
        pygame.init()
        self.window = Window(config.GAME_WIDTH, config.GAME_HEIGHT)
        self.hero = Hero(config.RESPAWN_POSITION_X, config.RESPAWN_POSITION_Y, "assets/kasia.png")
        self.obstacles = Obstacles()
        self.game_state = "running"
        self.score = 0
        self.best_score = 0

    def check_score(self, obstacles, hero):
        for obstacle in obstacles:
            if obstacle.position.x <= hero.hitbox.x < obstacle.position.x + 1:
                self.score += 0.5
                if self.score % 1 == 0:
                    sound = pygame.mixer.Sound('assets/scored_point.mp3')
                    sound.play()

    def start_new_game(self):
        self.hero.hitbox.center = config.RESPAWN_POSITION_X, config.RESPAWN_POSITION_Y
        self.hero.velocity = 0
        self.obstacles.clear()
        self.score = 0
        self.obstacles.counter = 0
        self.game_state = "running"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if (event.key == K_SPACE or event.key == K_UP) and not self.game_state == "paused" and not self.game_state == "game_over":
                    self.hero.flap()
                elif (event.key == K_p or event.key == K_ESCAPE) and not self.game_state == "game_over":
                    self.game_state = "paused" if self.game_state == "running" else "running"
                elif event.key == K_ESCAPE:
                    self.start_new_game()

    def run(self):
        while True:
            start_time = pygame.time.get_ticks()

            self.handle_events()

            if self.game_state == "paused":
                print_paused(self.window.display_surface)
            elif self.game_state == "game_over":
                if self.score > self.best_score:
                    self.best_score = self.score
                print_game_over(self.window.display_surface, self.score, self.best_score)
            else:
                self.update_game()
    
            pygame.display.update()
            pygame.time.delay(1000 // config.FPS - (pygame.time.get_ticks() - start_time))

    def update_game(self):
        # Fill the window with the background color
        self.window.display_surface.fill(config.WHITE)

        # Generate and draw obstacles 
        self.obstacles.generate_obstacles()
        self.obstacles.draw(self.window.display_surface)
        self.obstacles.update()
        
        # Check for collisions
        if self.hero.check_collision(self.obstacles.get_obstacles()):
            self.game_state = "game_over"
            sound = pygame.mixer.Sound('assets/ouch.mp3')
            sound.play()
        else:
            self.hero.draw(self.window.display_surface)
            self.hero.update()
            
        # Check score
        self.check_score(self.obstacles.get_obstacles(), self.hero)
        if not self.game_state == "game_over": 
            print_score(self.window.display_surface, self.score)