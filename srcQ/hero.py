import pygame
import math
import srcQ.config as config


class Hero:
    def __init__(self, brain):
        self.image = pygame.image.load('assets/kasia.png')
        self.image = pygame.transform.scale(self.image, (config.HERO_SIZE))
        self.hitbox = self.image.get_rect() 
        self.hitbox.center = (config.RESPAWN_POSITION_X, config.RESPAWN_POSITION_Y) 
        self.velocity = 0 
        self.gravity = config.GRAVITY  
        self.flap_strength = config.FLAP_STRENGTH 
        self.dead = False 
        self.score = 0
        self.state = (12, 8, 0)
        self.brain = brain 

    def flap(self):
        self.velocity = self.flap_strength

    def update(self, obstacles):
        self.velocity += self.gravity
        self.hitbox.y += self.velocity
        self.score += 1
        self.check_passed_obstacle(obstacles)
        self.update_brain(self.brain.reward, obstacles)

    def update_brain(self, reward, obstacles):
        next_obstacle = obstacles.next_obstacle(self)
        prev_state = self.state
        
        x_state = min(config.GAME_WIDTH, next_obstacle.position.x)
        x_state = math.floor(x_state / 80) + 2

        y_delta = next_obstacle.top - self.hitbox.top
        if y_delta < 0:
            y_delta = int(abs(y_delta) + config.GAME_HEIGHT * 0.8)
        
        if y_delta > config.GAME_HEIGHT * 0.8:
            y_state = 6 # todo fix jumping over obstacle (roof)
        else:
            y_state = math.floor(y_delta / 60)
        
        #print(x_state, y_state)
        action = self.brain.select_action(self.state)
        self.state = (x_state, y_state, action)
        self.brain.updateQ(prev_state, self.state, reward)
        
        if action == 1:
            self.flap()

    def check_passed_obstacle(self, obstacles):
        self.score += 1

    def get_distance_to_next_obstacle(self, obstacles):
        next_obstacle = obstacles.next_obstacle(self)
        if next_obstacle:
            return next_obstacle.position.x - self.hitbox.x, next_obstacle.top - self.hitbox.y

    def draw(self, surface, obstacles):
        next_obstacle = obstacles.next_obstacle(self)

        surface.blit(self.image, self.hitbox)

        # Draw lines to the next obstacle for debugging
        if next_obstacle:
            pygame.draw.line(surface, config.BLUE, (self.hitbox.centerx, self.hitbox.centery), (next_obstacle.position.x, next_obstacle.top), 2)

    def check_collision(self, obstacles):
        obstacles_list = obstacles.get_obstacles()
        # Check for collision with obstacle hitboxes
        for obstacle in obstacles_list:
            if self.hitbox.colliderect(obstacle.position): 
                self.update_brain(self.brain.punish, obstacles)
                self.dead = True 

        # Check for collision with screen boundaries
        if self.hitbox.top < 0 or self.hitbox.bottom > config.GAME_HEIGHT:
            self.update_brain(self.brain.punish, obstacles)
            self.dead = True