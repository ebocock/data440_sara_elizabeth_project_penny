# Project Penny : Monte-Carlo Simulation

## Background
The Penny's Game is a sequence game played between two players using a penny. During gameplay Player 1 selects a sequence of heads and tails, and Player 2 selects a different sequence of heads and tails. A penny is then tossed until one of the players' sequence of heads or tails appears, and the player who's sequence appears first wins.

The Humble-Nishiyama (H-N) Randomness Game is a variation of the Penney's Game which uses a standard deck of 52 playing cards, and the colors red/black in place of a penny. Each player selects a sequence, and then cards are drawn from the deck. If a player's sequence is drawn they score a trick. The player with the most tricks at the end of the deck of cards is the winner.

This project also investigates the 'Ron Version' of the Penney's game, which is played the same way as the H-N game, except it is scored by number of cards. As cards are drawn they form a pile, and when a player's sequence appears, they take all the cards in the pile. The player with the most cards at the end of the deck wins.

For further information regarding the H-N and Penney Games consult [this](https://en.wikipedia.org/wiki/Penney%27s_game) Wikipedia page.
## Purpose
The purpose of this code is to simulate games of the H-N and 'Ron Version' games to determine the optimal strategies for a playre faced with each possible 3-bit combination from their opponent.

## How-To Run Code
This code is separated into four key modules:

- datagen.py: generates and stores the decks
- record_storing.py: helper functions to store the records of the scored games and the number of cards processed so far
- gameplay.py: contains the logic and functions to play the games
- datavis.py: creates the heatmap visualizations with the win probability results from the simulations 

The main.py prompts the user to select between generating and scoring more decks and displaying the updated results heatmaps.
## Findings

