import pygame
import srcAI.config as config

def print_fps(surface, fps):
    font = pygame.font.Font(None, 24)
    text = font.render("FPS: " + str(fps), True, config.RED)
    text_position = text.get_rect(center=config.FPS_POSITION)
    surface.blit(text, text_position)

def print_alive_counter(surface, alive_counter):
    font = pygame.font.Font(None, 24)
    text = font.render("Alive: " + str(alive_counter), True, config.RED)
    text_position = text.get_rect(center=config.ALIVE_COUNTER_POSITION)
    surface.blit(text, text_position)

def print_score(surface, score):
    font = pygame.font.Font(None, 24)
    text = font.render("Score: " + str(score), True, config.RED)
    text_position = text.get_rect(center=config.SCORE_POSITION)
    surface.blit(text, text_position)

# Print information about distances and velocity (for debugging)
def print_information(surface, hero):
    font = pygame.font.Font(None, 24)

    text = font.render("Distance to next obstacle: " + str(int(hero.distance_to_next_obstacle)), True, config.RED)
    text_position = text.get_rect(center=(config.INFORMATION_POSITION_X, config.INFORMATION_POSITION_Y))
    surface.blit(text, text_position)

    text = font.render("Distance to next obstacle top: " + str(int(hero.distance_to_next_obstacle_top)), True, config.RED)
    text_position = text.get_rect(center=(config.INFORMATION_POSITION_X, config.INFORMATION_POSITION_Y + 50))
    surface.blit(text, text_position)

    text = font.render("Distance to next obstacle bottom: " + str(int(hero.distance_to_next_obstacle_bottom)), True, config.RED)
    text_position = text.get_rect(center=(config.INFORMATION_POSITION_X, config.INFORMATION_POSITION_Y + 100))
    surface.blit(text, text_position)

    text = font.render("Velocity: " + str(int(hero.velocity)), True, config.RED)
    text_position = text.get_rect(center=(config.INFORMATION_POSITION_X, config.INFORMATION_POSITION_Y + 150))
    surface.blit(text, text_position)