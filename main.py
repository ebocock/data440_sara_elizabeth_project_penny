#imports
from src.datagen import more_decks()
from src.datavis import display_heatmaps

# Process the n more decks
def process_cards():
    pass


# Main
def main():
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
            heatmap_q = input(f'Just processed {n_decks}, input 0 to display updated heatmaps.')
            if heatmap_q == '0':
                display_heatmaps()

if __name__ == "__main__":
    main()