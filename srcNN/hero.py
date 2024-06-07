import pygame
import srcNN.config as config

class Hero:
    def __init__(self):
        self.image = pygame.image.load('assets/kasia.png')
        self.image = pygame.transform.scale(self.image, (config.HERO_SIZE))
        self.hitbox = self.image.get_rect() 
        self.hitbox.center = (config.RESPAWN_POSITION_X, config.RESPAWN_POSITION_Y) 
        self.velocity = 0 
        self.gravity = config.GRAVITY  
        self.flap_strength = config.FLAP_STRENGTH 
        self.distance_to_next_obstacle = 0  # Distance to the middle of the next obstacle
        self.distance_to_next_obstacle_top = 0  # Distance to the top of the next obstacle
        self.distance_to_next_obstacle_bottom = 0  # Distance to the bottom of the next obstacle
        self.dead = False 
        self.ticks_alive = 0 

    def flap(self):
        self.velocity = self.flap_strength

    def update(self):
        self.velocity += self.gravity
        self.hitbox.y += self.velocity
        self.ticks_alive += 1

    def draw(self, surface, obstacles):
        surface.blit(self.image, self.hitbox)

        next_obstacle = obstacles.next_obstacle(self)

        # Draw lines to the next obstacle for debugging
        if next_obstacle:
            pygame.draw.line(surface, config.BLUE, (self.hitbox.centerx, self.hitbox.centery), (next_obstacle.position.x, next_obstacle.top), 2)
            pygame.draw.line(surface, config.BLUE, (self.hitbox.centerx, self.hitbox.centery), (next_obstacle.position.x, next_obstacle.bottom), 2)

    def check_collision(self, obstacles):
        # Check for collision with obstacle hitboxes
        for obstacle in obstacles:
            if self.hitbox.colliderect(obstacle.position): 
                self.dead = True 

        # Check for collision with screen boundaries
        if self.hitbox.top < 0 or self.hitbox.bottom > config.GAME_HEIGHT:
            self.dead = True
    
    def get_distance_to_next_obstacle(self, obstacles):
        next_obstacle = obstacles.next_obstacle(self)
        
        if next_obstacle:
            self.distance_to_next_obstacle = next_obstacle.position.x - self.hitbox.centerx
            self.distance_to_next_obstacle_top = next_obstacle.top - self.hitbox.top
            self.distance_to_next_obstacle_bottom = next_obstacle.bottom - self.hitbox.top