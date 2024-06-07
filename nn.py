from copy import deepcopy
from srcNN.game import Game
from srcNN.neural_network import NeuralNetwork
import srcNN.config as config

if __name__ == "__main__":
    # Create an initial population of random neural networks
    population = [NeuralNetwork(config.NEURAL_NETWORK_ARCHITECTURE) for _ in range(config.GENERATION_SIZE)]
    gen_number = 1

    # Load the best agent
    #population[0] = Game.load_best_agent(Game, "best_agent_30902.pkl")

    while True:
        game = Game()

        # Run the game with the current generation of neural networks and get the best 2 networks and the best score
        best_network, best_network2, best_score = Game.run(game, population)

        print(f"Generation {gen_number} best score: {best_score}")

        # Create the next generation of neural networks based on the best network
        next_generation = [deepcopy(best_network)]

        # Add to the next generation 20% random neural networks to avoid local minima
        for _ in range(int(config.GENERATION_SIZE * config.RANDOM_GENERATION_RATIO)):
            next_generation.append(NeuralNetwork(config.NEURAL_NETWORK_ARCHITECTURE))

        # Add to the next generation the remaining neural networks based on the crossover of the best 2 networks and mutation
        for _ in range(config.GENERATION_SIZE - len(next_generation)):
            parent1, parent2 = best_network, best_network2

            child = deepcopy(parent1)
            child.crossover(parent2)
            child.mutate(config.MUTATION_RATE)
            next_generation.append(child)

        # Update the generation
        population = next_generation
        gen_number += 1