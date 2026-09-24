# makes visualizations from output matrices
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from src.record_storing import get_probabilities, get_deck_count

#generate some dummy data
# regular_wins = np.random.rand(8, 8)
# ron_wins = np.random.rand(8,8)
# regular_ties = np.random.rand(8,8)
# ron_ties = np.random.rand(8,8)
# n_decks = 100000


#function to make visualization, generic 
def make_visualization(wins: np.ndarray, ties: np.ndarray, n_decks: int, title: str, score: str) -> plt.Figure:
    '''
    This is the function that creates a heatmap according to the project specifications and stores it.
    '''
    # create the diagonal mask so the invalid games can be grey
    mask = np.eye(wins.shape[0])


    # Create labels wtih win prob (tie prob)
    labels = np.empty(wins.shape, dtype=object)

    for i in range(wins.shape[0]):
        for j in range(wins.shape[1]):
            labels[i, j] = f"{wins[i, j]:.0f} ({ties[i, j]:.0f})"



    fig, ax = plt.subplots()
    sns.heatmap(wins,
            mask=mask,
            annot = labels,
            cmap = 'Blues',
            fmt = '',
            cbar = False,
            linewidths = 1,
            linecolor = 'white')
    ax.set_facecolor('lightgray')

    ax.set_xlabel('My Choice')
    ax.set_ylabel('Opponent Choice')
    ax.set_title(f'Probability of Win(Tie)\n{title}\nScored by {score}\n N = {n_decks}')
    plt.tight_layout()
    # saves the heatmap to display
    fig.savefig(f'figures/{title}heatmap.png', dpi=300, bbox_inches='tight')
    #saves for records to see convergence
    fig.savefig(f'figures/heatmap_records/{n_decks}_{title}.png', dpi = 300, bbox_inches = 'tight')
    return fig

# wrapper functions so that we can keep the make visualizations vague but still make title changes
# I used chatgpt to help me make these
def make_regular_visualization(wins: np.ndarray, ties: np.ndarray , n_decks:int)-> plt.Figure:
    '''
    This is a wrapper function that had the title and scoring methood for the regular game,
    so I did not have to make two separate functions to perform the same task.
    '''
    title = 'H-N Game'
    score = 'tricks'
    return make_visualization(wins, ties, n_decks, title, score)


def make_ron_visualization(wins: np.ndarray, ties: np.ndarray , n_decks:int)-> plt.Figure:
    '''
    This is a wrapper function that had the title and scoring methood for the ron version of the game,
    so I did not have to make two separate functions to perform the same task.
    '''
    title = "Ron's Variation"
    score = 'cards'
    return make_visualization(wins, ties, n_decks, title, score)

def display_heatmaps()-> None:
    '''
    This function gets the data, makes the visualizations, and shows the visualizations once they 
    are made
    '''
    # get data using the helper functions from record_storing.py
    regular_wins, regular_ties, ron_wins, ron_ties = get_probabilities()
    n_decks = get_deck_count()
    # make regular heatmap
    fig_1 = make_regular_visualization(regular_wins, regular_ties, n_decks)
    plt.show()
    # make ron heatmap
    fig_2 = make_ron_visualization(ron_wins, ron_ties, n_decks)
    plt.show
    return