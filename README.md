# Flappy Bird AI

This project implements an artificial intelligence (AI) to play a clone of the popular game Flappy Bird using neural networks and genetic algorithms. The AI learns to play the game by evolving generations of neural networks that control the bird's actions.

Additionally, it includes the implementation of a clone of the Flappy Bird game, allowing users to play the game manually or observe the AI's performance.

## Requirements

- Pygame library (`pip install pygame`)

## How it Works

The AI utilizes neural networks to make decisions for the hero's actions (flapping). Here's a brief overview of the process:

1. **Initialization**: An initial population of random neural networks is created.

2. **Game Execution**:
    - The game is executed with each neural network in the population.
    - The AI collects data on the performance of each network based on the game score and duration of survival.

3. **Selection**:
    - The best-performing networks are selected to form the next generation.
    - Some random networks are also added to prevent getting stuck in local minima.

4. **Crossover and Mutation**:
    - The remaining slots in the next generation are filled by combining the characteristics of the best networks through crossover and introducing random mutations.

5. **Repeat**:
    - Steps 2 to 4 are repeated for multiple generations until the AI achieves satisfactory performance.

## Game Controls

- Press `+` to increase game speed.
- Press `-` to decrease game speed.
- Press `ESC` to quit the game.
