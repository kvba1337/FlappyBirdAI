import pygame
from pygame.locals import *
from srcAI.window import Window 
from srcAI.hero import Hero 
from srcAI.obstacle import Obstacles  
from srcAI.overlay import print_fps, print_alive_counter, print_score, print_information 
from srcAI.neural_network import Matrix
import srcAI.config as config 

# Method to normalize a value between -1 and 1
def normalize(value, min_in, max_in, min_out=-1, max_out=1):
    value -= min_in
    value /= (max_in - min_in)
    value *= (max_out - min_out)
    value += min_out
    return value

class Game:
    def __init__(self):
        pygame.init()
        self.window = Window(config.GAME_WIDTH, config.GAME_HEIGHT)
        self.heroes = []
        self.obstacles = Obstacles()
        self.FPS = config.FPS
        self.alive_counter = 0
        self.score = 0

    def over(self):
        for hero in self.heroes:
            if not hero.dead:
                return False
        return True

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
                    if self.FPS > config.FPS // 10:
                        self.FPS //= 2  # Decrease FPS
    
    def make_flap_decision(self, hero, networks):
        # Update each hero's actions based on its neural network
        for hero, network in zip(self.heroes, networks):
            if hero.dead:
                continue
            else:
                self.alive_counter += 1

            hero.get_distance_to_next_obstacle(self.obstacles)

            # Prepare input data for the neural network
            normalized_distance_to_next_obstacle = normalize(hero.distance_to_next_obstacle, 0, 200, 0, 1)
            normalized_distance_to_next_obstacle_top = normalize(hero.distance_to_next_obstacle_top, -200, 200)
            normalized_distance_to_next_obstacle_bottom = normalize(hero.distance_to_next_obstacle_bottom, -200, 200)
            normalized_velocity = normalize(hero.velocity, -10, 10)
            
            input_data = [normalized_distance_to_next_obstacle_top, 
                          normalized_distance_to_next_obstacle_bottom, 
                          normalized_distance_to_next_obstacle, 
                          -normalized_velocity]
            #print (input_data)

            # Feed input data to the neural network and make decisions based on the output
            result_matrix = network.solve(Matrix.generate_from_row(input_data))

            if result_matrix.data[0][0] > config.ACTIVATION_THRESHOLD:
                hero.flap()
    
    def run(self, networks):
        # Create Hero objects for each neural network
        heroes = [Hero() for _ in range(len(networks))]
        for hero in heroes:
            self.heroes.append(hero)

        while not self.over():
            start_time = pygame.time.get_ticks()
            self.alive_counter = 0
            self.score += 1

            self.handle_events()
            self.make_flap_decision(self.heroes, networks)
            self.update_game()
            pygame.display.update()
            pygame.time.delay(1000 // self.FPS - (pygame.time.get_ticks() - start_time))
                
        # Calculate 2 best scores
        scores = [hero.ticks_alive for hero in self.heroes]
        best_scores = sorted(scores, reverse=True)[:2]

        # Return the best two neural networks and the best score
        return (networks[scores.index(best_scores[0])], 
                networks[scores.index(best_scores[1])], 
                best_scores[0])

    def update_game(self):
        self.window.display_surface.fill(config.WHITE)
        self.obstacles.generate_obstacles()
        self.obstacles.draw(self.window.display_surface)
        self.obstacles.update()
        
        for hero in self.heroes:
            if not hero.dead:
                hero.check_collision(self.obstacles.get_obstacles())
                hero.draw(self.window.display_surface, self.obstacles)
                hero.update()

        print_alive_counter(self.window.display_surface, self.alive_counter)
        print_fps(self.window.display_surface, self.FPS)
        print_score(self.window.display_surface, self.score)