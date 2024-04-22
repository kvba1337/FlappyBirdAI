import pygame
import src.myconstants as myconstants

class Score:
    def __init__(self):
        self.score = 0

    def check_score(self, obstacles, hero):
        for obstacle in obstacles:
            if obstacle.position.x <= hero.hitbox.x < obstacle.position.x + 1:
                self.score += 0.5
                if self.score % 1 == 0:
                    sound = pygame.mixer.Sound('assets/scored_point.mp3')
                    sound.play()

    def display_score(self, window):
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(int(self.score)), True, myconstants.GREEN) 
        text_position = score_text.get_rect(center=myconstants.SCORE_POSITION)
        window.window.blit(score_text, text_position)