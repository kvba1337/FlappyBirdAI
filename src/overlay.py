import pygame
import src.config as config

def print_score(surface, score):
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(int(score)), True, config.GREEN) 
    text_position = score_text.get_rect(center=config.SCORE_POSITION)
    surface.blit(score_text, text_position)

def print_game_over(surface, score, best_score):
    font = pygame.font.Font(None, 48)  
    game_over_text = font.render("Game Over", True, config.RED) 
    text_position = game_over_text.get_rect(center=(config.GAME_OVER_POSITION_X, config.GAME_OVER_POSITION_Y))  
    surface.blit(game_over_text, text_position)

    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(int(score)), True, config.GREEN)
    score_position = score_text.get_rect(center=(config.GAME_OVER_POSITION_X, config.GAME_OVER_POSITION_Y + 50)) 
    surface.blit(score_text, score_position)

    score_text = font.render("Best Score: " + str(int(best_score)), True, config.GREEN)
    score_position = score_text.get_rect(center=(config.GAME_OVER_POSITION_X, config.GAME_OVER_POSITION_Y + 100)) 
    surface.blit(score_text, score_position)

    text = font.render("Press ESC to continue", True, config.RED)
    text_position = text.get_rect(center=(config.GAME_OVER_POSITION_X, config.GAME_OVER_POSITION_Y + 150))  
    surface.blit(text, text_position)

def print_paused(surface):
    font = pygame.font.Font(None, 36)
    pause_text = font.render("Paused", True, config.RED)
    pause_position = pause_text.get_rect(center=config.PAUSE_POSITION)
    surface.blit(pause_text, pause_position)