from pathlib import Path
import numpy as np
#for reference later, on loading data https://stackoverflow.com/questions/48429408/open-and-view-npz-file-in-python


PATH_SCORE_RECORDS = Path("data/score_records")
PATH_RESULT_COUNTS = PATH_SCORE_RECORDS/"result_counts.npz"
PATH_PROBABILITIES = PATH_SCORE_RECORDS/"probabilities.npz"
PATH_DECK_COUNT = PATH_SCORE_RECORDS / "total_decks.txt"

PATH_SCORE_RECORDS.mkdir(parents=True, exist_ok=True)

#used following source for below code https://www.geeksforgeeks.org/python/how-to-save-multiple-numpy-arrays/
def save_result_counts(score_grids) -> None:
    og_wins_grid,og_ties_grid,ron_wins_grid,ron_ties_grid,counter_grid = score_grids
    np.savez(PATH_RESULT_COUNTS,og_wins_grid=og_wins_grid, og_ties_grid = og_ties_grid, ron_wins_grid = ron_wins_grid ,ron_ties_grid=ron_ties_grid,counter_grid= counter_grid)

    return

def save_probabilities(score_grids) -> None:
#https://www.reddit.com/r/learnpython/comments/9ern4w/numpys_npdivide_has_a_where_parameter_and_i_would/
#https://numpy.org/devdocs/reference/generated/numpy.divide.html
#https://www.reddit.com/r/learnpython/comments/4dwm19/how_should_i_initialize_a_numpy_array_of_nan/
    og_wins_grid,og_ties_grid,ron_wins_grid,ron_ties_grid,counter_grid = score_grids
    
    percent_og_wins = np.full((8,8),np.nan)
    percent_og_ties = np.full((8,8),np.nan)

    np.divide(og_wins_grid, counter_grid, out = percent_og_wins, where = counter_grid!=0)
    np.divide(og_ties_grid, counter_grid, out = percent_og_ties, where = counter_grid!=0)
    percent_og_wins*=100
    percent_og_ties*=100


    percent_ron_wins = np.full((8,8),np.nan)
    percent_ron_ties = np.full((8,8),np.nan)

    np.divide(ron_wins_grid, counter_grid, out = percent_ron_wins, where= counter_grid !=0)
    np.divide(ron_ties_grid, counter_grid, out = percent_ron_ties, where= counter_grid !=0)
    percent_ron_wins*=100
    percent_ron_ties*=100


    np.savez(PATH_PROBABILITIES,percent_og_wins=percent_og_wins, percent_og_ties = percent_og_ties, percent_ron_wins = percent_ron_wins ,percent_ron_ties=percent_ron_ties)
    return

#https://note.nkmk.me/en/python-numpy-load-save-savez-npy-npz/
def get_result_counts() -> tuple:
    
    if not PATH_RESULT_COUNTS.exists():
        return np.zeros((8,8)),np.zeros((8,8)),np.zeros((8,8)),np.zeros((8,8)),np.zeros((8,8))
    
    with np.load(PATH_RESULT_COUNTS) as result_counts:
        og_wins_grid = result_counts["og_wins_grid"]
        og_ties_grid = result_counts["og_ties_grid"]
        
        ron_wins_grid = result_counts["ron_wins_grid"]
        ron_ties_grid = result_counts["ron_ties_grid"]
        counter_grid = result_counts["counter_grid"]
        return og_wins_grid,og_ties_grid,ron_wins_grid,ron_ties_grid,counter_grid


# this stores the total number of cards processed
def update_deck_count(num_decks: int) -> None:
    '''
    This function updates the record that contains the number of decks that has
    been processed so far. I used chatgpt to help me make it.
    '''
    if PATH_DECK_COUNT.exists():
        with open(PATH_DECK_COUNT, "r") as f:
            total_decks = int(f.read())
    else:
        total_decks = 0

    total_decks += num_decks

    with open(PATH_DECK_COUNT, "w") as f:
        f.write(str(total_decks))

    return

def get_deck_count() -> int:
    '''
    This function retrieves the number of decks processed so far.
    '''
    if not PATH_DECK_COUNT.exists():
        return 0

    with open(PATH_DECK_COUNT, "r") as f:
        total_decks = int(f.read())

    return total_decks

def get_probabilities() -> tuple:
    '''
    Similar to get results count this function returns the most recent probabilities.
    '''
    if not PATH_PROBABILITIES.exists():
        return (
            np.zeros((8,8)),
            np.zeros((8,8)),
            np.zeros((8,8)),
            np.zeros((8,8))
        )

    with np.load(PATH_PROBABILITIES) as probabilities:
        percent_og_wins = probabilities["percent_og_wins"]
        percent_og_ties = probabilities["percent_og_ties"]
        percent_ron_wins = probabilities["percent_ron_wins"]
        percent_ron_ties = probabilities["percent_ron_ties"]

        return (
            percent_og_wins,
            percent_og_ties,
            percent_ron_wins,
            percent_ron_ties
        )