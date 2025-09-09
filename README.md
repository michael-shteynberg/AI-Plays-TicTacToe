# Tic-Tac-Toe AI: Minimax Algorithm

An unbeatable Tic-Tac-Toe AI using minimax algorithm for perfect game play through adversarial search.

## Overview

This AI achieves optimal play by exploring all possible game outcomes before making each move. Using game theory and exhaustive search, it guarantees the best possible result - never losing, only winning or drawing.

## Key AI Concepts

### Minimax Algorithm
The AI uses minimax, a decision rule for zero-sum games where one player's gain equals the opponent's loss. The algorithm recursively evaluates all possible future game states, with X maximizing the score and O minimizing it. This mutual antagonism drives both players toward optimal strategies.

### Game Tree Search
The system constructs a complete game tree from the current position to all terminal states. Each node represents a board configuration, edges represent moves, and leaves contain final outcomes. The AI traverses this tree using depth-first search to evaluate every possible game continuation.

### Perfect Information Games
Tic-Tac-Toe exemplifies perfect information games where all game state is visible and outcomes are deterministic. This allows the AI to achieve perfect play - guaranteed optimal decisions without uncertainty or randomness affecting strategy.

### Utility Functions
Terminal states are evaluated numerically: +1 for X wins, -1 for O wins, 0 for draws. This quantification enables mathematical optimization, transforming qualitative outcomes into values the algorithm can maximize or minimize.

### Adversarial Search
The AI assumes both players act rationally to optimize their outcomes. This adversarial model, where players have opposing goals, forms the foundation for game-playing AI from chess engines to modern game bots.

## Why This Matters

- **Game Theory Foundation**: Core concepts applicable to economics, military strategy, and decision theory
- **Search Algorithms**: Fundamental techniques used throughout AI
- **Optimal Decision Making**: Guaranteed best play through exhaustive analysis
- **Classical AI**: Demonstrates symbolic reasoning without machine learning
