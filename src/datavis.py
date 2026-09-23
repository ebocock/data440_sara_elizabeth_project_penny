# makes visualizations from output matrices
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#generate some dummy data
regular_wins = np.random.rand(8, 8)
ron_wins = np.random.rand(8,8)
regular_ties = np.random.rand(8,8)
ron_ties = np.random.rand(8,8)
n_decks = 100000

#function to get the data
def get_data():
    return regular_wins, ron_wins, regular_ties, ron_ties

#function to make visualization, generic 
def make_visualization(wins, ties, n_decks):
# Determine title
    if wins is ron_wins:
        title = "Ron's Variation"
        score = 'cards'
    else:
        title = 'H-N Game'
        score = 'tricks'

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
    fig.savefig(f'figures/{title}_{n_decks}heatmap.png', dpi=300, bbox_inches='tight')
    return fig


#function to show visualization
def main():
    regular_wins, ron_wins, regular_ties, ron_ties = get_data()
    fig = make_visualization(ron_wins,
                       ron_ties,
                       n_decks)
    plt.show()

if __name__ == "__main__":
    main()