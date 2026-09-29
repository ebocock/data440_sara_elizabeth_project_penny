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
Both of these games have a second-player advantage. This means that faced with the first player's choice, the second player can always choose a strategty that will make them more likely to win.
### H-N Game
In the H-N game, the optimal strategy for the first player is to select either BRB or RBR because those have the lowest max win probabiltiy for the second player, assuming that player is rational and acting optimally (80% win prob for player 2, 8% tie prob, so a 12% win prob for player 1).

The optimal choice for the second player is to select whichever strategy gives them the highest win probability based on their opponent's choice. Using the above optimal strategies, if the first player selects BRB, the second player should select BBR, which gives them an 80% chance of winning. If the first player selects RBR then the second player should select RRB, wich also gives them an 80% chance of winning.

### Ron's Version
In the Ron version of the game, since it is scored based on the number of cards rhater than tricks the probability of tie is greatly decreased, although the significant second player advantage remains.

Playing optimally, the first player will still select either BRB or RBR, but there is a change in the probabilities. Assuming the second player is rational and playing optimally the proability of winning for player 1 falls to 7%, with a 1% tie probability and a 92% win probability for player two.

The optimal strategy for the second player is to select whichever strategy gives them the highest probability of winning. Faced with optimal strategies for the first player, the second player should select BBR if the first player selects RBR and RRB if the first player selects BRB.