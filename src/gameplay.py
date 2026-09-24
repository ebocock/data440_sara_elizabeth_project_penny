import numpy as np 
import random
from src.datagen import generate_decks #import deck generation from src
from src.record_storing import save_result_counts, save_probabilities, get_result_counts, update_deck_count


def convert_deck(deck_array) -> str: #makes array of 1s,0s, a string, returns string
  deck_string = "" 

  for card in deck_array: #convert to string card by card ie character by character

    if card == 1: #1s are changed to red
      color = "R"
    else:
      color = "B" #0s are changed to black

    deck_string += color #add converted card to strinf

  return deck_string #return string

def run_og_game(deck, mychoice, oppchoice ) -> str: #HN version of the game, scores by tricks 
  mytricks=0 #tracks the number of tricks ive won
  opptricks=0 # tracks the number of tricks opponent has won

  drawn="" #stores all the drawn cards

  for card in deck:
    drawn += card #add thw next card to drawn pile

    if drawn.endswith(mychoice): #if drawn crd pile ended w my sequence
      mytricks+=1 #add a point for winning
      drawn = "" #reset drawn pile

    elif drawn.endswith(oppchoice):  #same as above but for opponent
      opptricks+=1
      drawn = ""

  if mytricks > opptricks: #if my trick number wins i win the game
   return "win" 
  elif mytricks ==opptricks: # if i tie, return tie string
    return "tie"
  else:
    return "loss" # losses arent necessarily tracked, but adding for readibility


def run_ron_game(deck, mychoice, oppchoice) -> str: #rons version of the game, scored by won cards
  mycards =0 #tracks the number of tricks ive won
  oppcards=0 # tracks the number of tricks opponent has won

  drawn="" #stores all the drawn cards

  for card in deck:
    drawn += card #add the next card to drawn pile

    if drawn.endswith(mychoice): #if drawn crd pile ended w my sequence
      mycards += len(drawn)  #whole pile awared to me
      drawn = "" # reset drawn pile

    elif drawn.endswith(oppchoice): 
      oppcards+= len(drawn) # whole pile awarded to opponennt
      drawn = ""

  if mycards > oppcards: # if i have more cards i win the game
   return "win"
  elif mycards == oppcards: #if we have equal number of cards we tie the gae
    return "tie"
  else:
    return "loss" #loss string still returned for readiblity


def play_n_score(deck_array, og_wins_grid, og_ties_grid, ron_wins_grid, ron_tie_grid, counter_grid, combos) -> None: #plays the actual games, adds points for scores
    
    deck_string = convert_deck(deck_array) #change array to string

    for mychoice in combos: #iterate through all my card choice combinations
      for oppchoice in combos:  #iterate through all opponenet card combinations

        if mychoice != oppchoice: # runs games when me and oponenent havent picked same combination
          og_outcome = run_og_game(deck_string, mychoice, oppchoice)
          ron_outcome = run_ron_game(deck_string, mychoice, oppchoice)

# consulted Claude for logic/structure of below 11 lines
          m = combos.index(mychoice)
          o = combos.index(oppchoice)
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

combos = ["BRR", "BRB", "BBR", "BBB", "RRR","RRB","RBR","RBB"] #all possible combos, listed to record for results tracking


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
