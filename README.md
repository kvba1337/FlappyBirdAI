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

https://github.com/user-attachments/assets/97fdda5f-c1da-4692-b8e1-14c4747b2af7 

https://github.com/user-attachments/assets/2d04eac7-fd77-4095-9700-c4215fa339b8

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
