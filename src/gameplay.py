import numpy as np 
import random
from src.datagen import generate_decks #import deck generation from src
from src.record_storing import save_result_counts, save_probabilities, get_result_counts, update_deck_count


def convert_deck(deck_array) -> str: #makes array of 1s,0s, a string, returns string
  deck_string = "".join(deck_array.astype(str))
  return deck_string #return string


def run_game(deck, mychoice, oppchoice) -> str: #rons version of the game, scored by won cards
  my_tricks = 0 #tracks the number of tricks ive won
  my_cards = 0 # tracks cards
  opp_tricks = 0 # tracks the number of tricks opponent has won
  opp_cards = 0 #tracks cards

  startidx = 0
  while True:

    myidx  = deck.find(mychoice, startidx)
    oppidx = deck.find(oppchoice, startidx)

    if myidx == -1 and oppidx == -1:
      break

    if oppidx == -1 or (myidx != -1 and myidx < oppidx):
      my_tricks += 1
      my_cards += (myidx - startidx +3)
      startidx = myidx+3

    else:
      opp_tricks += 1
      opp_cards += (oppidx - startidx +3)
      startidx = oppidx+3

  if my_cards > opp_cards:
    ron_result = "win"
  elif my_cards == opp_cards:
    ron_result = "tie"
  else:
    ron_result = "loss"

  if my_tricks > opp_tricks:
    reg_result = "win"
  elif my_tricks == opp_tricks:
    reg_result = "tie"
  else:
    reg_result = "loss"

  return reg_result, ron_result


def play_n_score(deck_array, og_wins_grid, og_ties_grid, ron_wins_grid, ron_tie_grid, counter_grid, combos) -> None: #plays the actual games, adds points for scores
    
    deck_string = convert_deck(deck_array) #change array to string

    for m, mychoice in enumerate(combos): #iterate through all my card choice combinations
      for o, oppchoice in enumerate(combos):  #iterate through all opponenet card combinations

        if mychoice != oppchoice: # runs games when me and oponenent havent picked same combination
          og_outcome, ron_outcome = run_game(deck_string, mychoice, oppchoice)

# consulted chatgpt for logic/structure of below 11 lines

          counter_grid[o,m] += 1

          if og_outcome == "win":
            og_wins_grid[o,m] += 1
          elif og_outcome == "tie":
            og_ties_grid[o,m] += 1

          if ron_outcome == "win":
            ron_wins_grid[o,m] += 1
          elif ron_outcome == "tie":
            ron_tie_grid[o,m] += 1

    return

# combos = ['BBB', 'BBR', 'BRB', 'BRR', 'RBB', 'RBR', 'RRB', 'RRR']
# above is a human-readable version of the below combos (0s mean black, 1s mean red)
combos = ['000', '001', '010', '011', '100', '101', '110', '111']

def fill_score_grids(decks) -> tuple:
  # source consulted for below chunk: https://www.geeksforgeeks.org/python/create-a-numpy-array-filled-with-all-zeros-python/
  #below generates grid to record wins and games
  og_wins_grid = np.zeros((8,8)) # for og game, 8 is for 8 total combination
  og_ties_grid = np.zeros((8,8)) # for og game, 8 is for 8 total combination
  ron_wins_grid = np.zeros((8,8)) #for ron game
  ron_ties_grid = np.zeros((8,8)) #for ron game
  counter_grid = np.zeros((8,8)) #all games

  for deck_array in decks: #play the games for every deck
    play_n_score(deck_array,og_wins_grid,og_ties_grid,ron_wins_grid,ron_ties_grid,counter_grid, combos) 

  return og_wins_grid,og_ties_grid,ron_wins_grid,ron_ties_grid,counter_grid

def score_saver(score_grids) -> None:
  save_result_counts(score_grids) #save the raw counts of wins and ties
  save_probabilities(score_grids) #save the win porbailities
  return

def process_added_decks(filepath):
  
  new_decks = np.load(filepath)
  new_grids = fill_score_grids(new_decks)
  old_grids = get_result_counts()

  og_wins_grid = old_grids[0] +new_grids[0]
  og_ties_grid = old_grids[1] +new_grids[1]
  
  ron_wins_grid = old_grids[2] +new_grids[2]
  ron_ties_grid = old_grids[3] +new_grids[3]
  counter_grid = old_grids[4] +new_grids[4]

  score_records = og_wins_grid,og_ties_grid,ron_wins_grid,ron_ties_grid,counter_grid
  score_saver(score_records)
  update_deck_count(len(new_decks))
  return
