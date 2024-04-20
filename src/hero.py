import pygame
import src.myconstants as myconstants

class Hero:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, myconstants.HERO_SIZE)
        self.hitbox = self.image.get_rect()
        self.hitbox.center = (x, y)
        self.velocity = 0
        self.gravity = myconstants.GRAVITY
        self.flap_strength = myconstants.FLAP_STRENGTH

    def flap(self):
        self.velocity = self.flap_strength

    def update(self):
        self.velocity += self.gravity
        self.hitbox.y += self.velocity

    def draw(self, surface):
        surface.blit(self.image, self.hitbox)

    def check_collision(self, obstacles):
        for obstacle in obstacles:
            if self.hitbox.colliderect(obstacle.position):
                return True
            
        if self.hitbox.top < 0 or self.hitbox.bottom > myconstants.GAME_HEIGHT:
            return True
        
        return False