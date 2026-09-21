import numpy as np 
import random
from datagen import generate_decks #import deck generation from src


def convert_deck(deck_array) -> str: #makes array of 1s,0s, a string, returns string
  deck_string = "" 

  for card in deck_array: #convert to string card by card ie character by character

    if card == 1: #1s are changed to red
      color = "R"
    else:
      color = "B" #0s are changed to black

    deck_string += color #add converted card to strinf

  return deck_string #return string

def run_og_game(deck, mychoice, oppchoice ) -> int: #HN version of the game, scores by tricks 
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

  if mytricks >= opptricks: #if my trick number wins or ties i win the game
   return 1 
  else:
    return 0

def run_ron_game(deck, mychoice, oppchoice ) -> int: #rons version of the game, scored by won cards
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

  if mycards >= oppcards: # if i win or tie i win the game
   return 1
  else:
    return 0


def play_n_score(deck_array, og_wins_grid, ron_wins_grid, counter_grid, combos) -> None:
    card_colors = "BR" 
    
    deck_string = convert_deck(deck_array)

    mychoice= "".join(random.choices(card_colors, k=3))
    oppchoice= "".join(random.choices(card_colors, k=3))

    if mychoice != oppchoice:
      og_outcome = run_og_game(deck_string, mychoice, oppchoice)
      ron_outcome = run_ron_game(deck_string, mychoice, oppchoice)


      m = combos.index(mychoice)
      o = combos.index(oppchoice)
      counter_grid[m,o] += 1
      og_wins_grid[m,o] += og_outcome
      ron_wins_grid[m,o] += ron_outcome

    return

decks, seed, filepath = generate_decks(n_cards=52, n_decks=1000) #generates 1000 decks to start with 
print(len(decks), "decks created using seed number",seed, "with filepath", filepath)

combos = ["BRR", "BRB", "BBR", "BBB", "RRR","RRB","RBR","RBB"] #all possible combos, listed to record for results tracking

#below generates grid to record wins and games
og_wins_grid = np.zeros((8,8)) # for og game, 8 is for 8 total combination
ron_wins_grid = np.zeros((8,8)) #for ron game
counter_grid = np.zeros((8,8)) #all games


for deck_array in decks: #play the games for every deck
  play_n_score(deck_array,og_wins_grid,ron_wins_grid,counter_grid, combos) 

