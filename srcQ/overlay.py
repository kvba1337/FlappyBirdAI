import pygame
import srcQ.config as config


def print_fps(surface, fps):
    font = pygame.font.Font(None, 24)
    text = font.render("FPS: " + str(fps), True, config.RED)
    text_position = text.get_rect(center=config.FPS_POSITION)
    surface.blit(text, text_position)


def print_score(surface, score, best_score):
    font = pygame.font.Font(None, 24)
    text = font.render("Score: " + str(score), True, config.RED)
    text_position = text.get_rect(center=config.SCORE_POSITION)
    surface.blit(text, text_position)

    font = pygame.font.Font(None, 24)
    text = font.render("Best score: " + str(best_score), True, config.RED)
    text_position = text.get_rect(center=(config.SCORE_POSITION[0] + 10, config.SCORE_POSITION[1] + 25))
    surface.blit(text, text_position)

def print_generation(surface, generation):
    font = pygame.font.Font(None, 24)
    text = font.render("Generation: " + str(generation), True, config.RED)
    text_position = text.get_rect(center=config.GENERATION_POSITION)
    surface.blit(text, text_position)