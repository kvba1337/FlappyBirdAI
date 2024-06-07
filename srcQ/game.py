import pygame
import pickle
from pygame.locals import *
from srcQ.window import Window 
from srcQ.hero import Hero 
from srcQ.obstacle import Obstacles  
from srcQ.overlay import print_fps, print_score, print_generation
from srcQ.qlearn import QLearn
import srcQ.config as config 


class Game:
    def __init__(self):
        pygame.init()
        self.window = Window(config.GAME_WIDTH, config.GAME_HEIGHT)
        self.qlearn = QLearn()
        self.hero = Hero(self.qlearn)
        self.obstacles = Obstacles()
        self.FPS = config.FPS
        self.score = 0
        self.best_score = 0
        self.generation = 1

    def start_game(self):
        self.hero = Hero(self.qlearn)
        self.obstacles = Obstacles()
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_EQUALS:
                    if self.FPS < config.FPS * 10:
                        self.FPS *= 2  # Increase FPS
                elif event.key == K_MINUS:
                    if self.FPS > config.FPS // 100:
                        self.FPS //= 2  # Decrease FPS

                elif event.key == K_SPACE:
                    self.hero.flap()
    
    def run(self):
        # Load the best agent
        #self.load_best_agent("best_agent_24941.pkl")
        
        while True:
            start_time = pygame.time.get_ticks()
            self.alive_counter = 0
            self.score += 1

            self.handle_events()
            self.update_game()

            pygame.display.update()
            pygame.time.delay(1000 // self.FPS - (pygame.time.get_ticks() - start_time))
                
    def update_game(self):
        self.window.display_surface.fill(config.WHITE)
        
        self.obstacles.generate_obstacles()
        self.obstacles.draw(self.window.display_surface)
        self.obstacles.update()
        
        self.hero.check_collision(self.obstacles)
        self.hero.draw(self.window.display_surface, self.obstacles)
        self.hero.update(self.obstacles)

        if self.hero.dead:
            self.generation += 1
            
            if self.score > self.best_score:
                self.best_score = self.score
                if self.best_score >= 20000:
                    self.save_best_agent(f"best_agent_{self.best_score}.pkl")
            
            self.start_game()

        print_fps(self.window.display_surface, self.FPS)
        print_score(self.window.display_surface, self.score, self.best_score)
        print_generation(self.window.display_surface, self.generation)

    def save_best_agent(self, filename):
        filepath = f"srcQ/best_agents/{filename}"
        with open(filepath, 'wb') as f:
            pickle.dump(self.qlearn.Q, f)

    def load_best_agent(self, filename):
        filepath = f"srcQ/best_agents/{filename}"
        with open(filepath, 'rb') as f:
            self.qlearn.Q = pickle.load(f)