# FlappyBirdAI

A Flappy Bird game clone with AI implementations using Q-Learning and Neural Networks.

## Features

- Classic Flappy Bird gameplay
- Q-Learning AI implementation
- Neural Network AI implementation with genetic algorithm
- Adjustable simulation speed
- Performance tracking

##  AI Implementations

### Q-Learning
- State space: Bird position relative to obstacles
- Actions: Flap or don't flap
- Reward system: Positive for survival, negative for collision

### Neural Network
- 4-layer neural network with genetic algorithm
- Input: Distance to obstacles and velocity
- Population-based training with mutations and crossover
- Best agents are saved automatically

## Demo

| Q-Learning                             | Neural Network                               |
| ----------------------------------- | --------------------------------------- |
| ![Q-Learning](docs/videos/q-learning.mp4) | ![Neural Network](docs/videos/neural-network.mp4) |


## Requirements

- Python 3.x
- Pygame

## How to Run

Choose one of the three gameplay options:

```bash
# Play manually
python user.py

# Run Q-Learning AI
python qlearning.py

# Run Neural Network AI with genetic algorithm
python nn.py
```

## Controls

**Manual Play:**
- `Space` / `Up Arrow` - Flap
- `P` / `Esc` - Pause/Resume
- `Esc` (when game over) - Restart

**AI Modes:**
- `+` - Increase simulation speed
- `-` - Decrease simulation speed
- `Esc` - Quit
