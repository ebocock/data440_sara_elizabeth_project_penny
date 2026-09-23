from pathlib import Path
import numpy as np
#for reference later, on loading data https://stackoverflow.com/questions/48429408/open-and-view-npz-file-in-python


PATH_SCORE_RECORDS = Path("data/score_records")
PATH_RESULT_COUNTS = PATH_SCORE_RECORDS/"result_counts.npz"
PATH_PROBABILITIES = PATH_SCORE_RECORDS/"probabilities.npz"

PATH_SCORE_RECORDS.mkdir(parents=True, exist_ok=True)

#used following source for below code https://www.geeksforgeeks.org/python/how-to-save-multiple-numpy-arrays/
def save_result_counts(og_wins_grid,og_ties_grid,ron_wins_grid,ron_tie_grid,counter_grid) -> None:
    np.savez(PATH_RESULT_COUNTS,og_wins_grid=og_wins_grid, og_ties_grid = og_ties_grid, ron_wins_grid = ron_wins_grid ,ron_tie_grid=ron_tie_grid,counter_grid= counter_grid)

    return

def save_probabilities(og_wins_grid,og_ties_grid,ron_wins_grid,ron_tie_grid,counter_grid) -> None:
#https://www.reddit.com/r/learnpython/comments/9ern4w/numpys_npdivide_has_a_where_parameter_and_i_would/
#https://numpy.org/devdocs/reference/generated/numpy.divide.html
#https://www.reddit.com/r/learnpython/comments/4dwm19/how_should_i_initialize_a_numpy_array_of_nan/
    percent_og_wins = np.full((8,8),np.nan)
    percent_og_ties = np.full((8,8),np.nan)

    np.divide(og_wins_grid, counter_grid, out = percent_og_wins, where = counter_grid!=0)
    np.divide(og_ties_grid, counter_grid, out = percent_og_ties, where = counter_grid!=0)
    percent_og_wins*=100
    percent_og_ties*=100


    percent_ron_wins = np.full((8,8),np.nan)
    percent_ron_ties = np.full((8,8),np.nan)

    np.divide(ron_wins_grid, counter_grid, out = percent_ron_wins, where= counter_grid !=0)
    np.divide(ron_tie_grid, counter_grid, out = percent_ron_ties, where= counter_grid !=0)
    percent_ron_wins*=100
    percent_ron_ties*=100


    np.savez(PATH_PROBABILITIES,percent_og_wins=percent_og_wins, percent_og_ties = percent_og_ties, percent_ron_wins = percent_ron_wins ,percent_ron_ties=percent_ron_ties)
    return