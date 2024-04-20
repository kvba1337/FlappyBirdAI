import pygame
import src.myconstants as myconstants

class GameState:
    def __init__(self):
        self.is_game_over = False
        self.is_paused = False
    
    def game_over(self, window, score):
        font = pygame.font.Font(None, 48)  
        game_over_text = font.render("Game Over", True, myconstants.RED) 
        text_position = game_over_text.get_rect(center=(myconstants.GAME_OVER_POSITION_X, myconstants.GAME_OVER_POSITION_Y))  
        window.window.blit(game_over_text, text_position)

        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(int(score.score)), True, myconstants.GREEN)
        score_position = score_text.get_rect(center=(myconstants.GAME_OVER_POSITION_X, myconstants.GAME_OVER_POSITION_Y + 50)) 
        window.window.blit(score_text, score_position)

        text = font.render("Press ESC to continue", True, myconstants.GREEN)
        text_position = text.get_rect(center=(myconstants.GAME_OVER_POSITION_X, myconstants.GAME_OVER_POSITION_Y + 100))  
        window.window.blit(text, text_position)

    def paused(self, window):
        font = pygame.font.Font(None, 36)
        pause_text = font.render("Paused", True, myconstants.BLACK)
        window.window.blit(pause_text, myconstants.PAUSE_POSITION)