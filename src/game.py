import pygame
from pygame.locals import *
import src.myconstants as myconstants
from src.background import Background
from src.hero import Hero
from src.obstacle import Obstacles
from src.window import Window
from src.game_state import GameState
from src.score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.window = Window(myconstants.GAME_WIDTH, myconstants.GAME_HEIGHT)
        self.background = Background(self.window.width, self.window.height)
        self.hero = Hero(myconstants.RESPAWN_POSITION_X, myconstants.RESPAWN_POSITION_Y, "assets/kasia.png")
        self.obstacles = Obstacles()
        self.game_state = GameState()
        self.clock = pygame.time.Clock()
        self.score = Score()
        self.mode = myconstants.MODE

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return True
            elif event.type == KEYDOWN:
                if event.key == K_SPACE or event.key == K_UP:
                    self.hero.flap()
                elif (event.key == K_p or event.key == K_ESCAPE) and not self.game_state.is_game_over:
                    self.game_state.is_paused = not self.game_state.is_paused
                elif event.key == K_ESCAPE:
                    self.obstacles.clear()
                    self.hero.hitbox.center = myconstants.RESPAWN_POSITION_X, myconstants.RESPAWN_POSITION_Y
                    self.score.score = 0
                    self.obstacles.counter = 0
                    self.game_state.is_game_over = False
                    self.hero.flap()

        return False

    def run(self):
        quit_game = False
        while not quit_game:
            quit_game = self.handle_events()

            if self.game_state.is_paused:
                self.game_state.paused(self.window)
            elif self.game_state.is_game_over:
                self.game_state.game_over(self.window, self.score)
            else:
                self.update_game()
    
            pygame.display.update()
            self.clock.tick(myconstants.FPS)

        pygame.quit()

    def update_game(self):
        # Fill the window with the background color
        self.window.window.fill(self.background.color)

        # Generate and draw obstacles 
        self.obstacles.generate_obstacles(self.window, self.mode)
        self.obstacles.draw(self.window.window)
        
        # Draw the hero
        self.hero.draw(self.window.window)
        
        # Check for collisions
        if self.hero.check_collision(self.obstacles.get_obstacles()):
            self.game_state.is_game_over = True
            sound = pygame.mixer.Sound('assets/ouch.mp3')
            sound.play()
        
        # Check score
        self.score.check_score(self.obstacles.get_obstacles(), self.hero)
        if not self.game_state.is_game_over: self.score.display_score(self.window)
        
        # Update the game state
        self.hero.update()
        self.obstacles.update(self.background)
        self.background.update()