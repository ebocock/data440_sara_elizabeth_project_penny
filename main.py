#imports
from src.datagen import generate_decks
from src.datavis import get_data, make_visualization
import matplotlib.pyplot as plt

#dummy for now
n_decks = 20
# Create/display up to date heatmaps
def display_heatmaps():
    # get data
    regular_wins, ron_wins, regular_ties, ron_ties = get_data()
    # make regular heatmap
    fig_1 = make_visualization(regular_wins, regular_ties, n_decks)
    plt.show()
    # make ron heatmap
    fig_2 = make_visualization(ron_wins, ron_ties)
    plt.show
    return

# Generate n more decks
def more_decks(n):
    print(f'Creating {n} more decks')
    decks, seed, filepath = generate_decks(52, n)
    print(f'{n} decks saved to {filepath}.')
    return

# Process the n more decks
def process_cards():
    pass


# Main
if __name__ == '__main__':
    print('Welcome to the Project Penny Simulation')
    first_action = input('Type 0 to display the most up-to-date heatmaps,\n type\n' \
    'Type 1 to generate more decks.')
    if first_action == '0':
        display_heatmaps()

    elif first_action == '1':
        n_decks = input('Enter the number of decks you would like to generate:')
        more_decks()
        process = input(f'You now have {n_decks} unprocessed decks.\n \
                        select 0 to process, select 1 to quit')
        if process == '0':
            process_cards()
            heatmap_q = input(f'Just processed {n_cards}, input 0 to display updated heatmaps.')
            if heatmap_q == '0':
                display_heatmaps()